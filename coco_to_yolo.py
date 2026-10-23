import json
import os
from pathlib import Path


def coco_to_yolo(
    coco_json_path,
    output_labels_dir,
    save_classes_txt=True,
    create_empty_txt=True
):
    """
    将 COCO 格式 json 标签转换为 YOLO 格式 txt 标签。

    COCO bbox格式:
        [x_min, y_min, width, height]

    YOLO bbox格式:
        class_id x_center y_center width height

    Args:
        coco_json_path: COCO格式json文件路径
        output_labels_dir: 输出YOLO txt标签文件夹
        save_classes_txt: 是否保存类别名称文件 classes.txt
        create_empty_txt: 对没有标注的图像是否创建空txt文件
    """

    coco_json_path = Path(coco_json_path)
    output_labels_dir = Path(output_labels_dir)
    output_labels_dir.mkdir(parents=True, exist_ok=True)

    if not coco_json_path.exists():
        raise FileNotFoundError(f"COCO json文件不存在: {coco_json_path}")

    # 读取COCO json
    with open(coco_json_path, "r", encoding="utf-8") as f:
        coco_data = json.load(f)

    images = coco_data.get("images", [])
    annotations = coco_data.get("annotations", [])
    categories = coco_data.get("categories", [])

    if not images:
        raise ValueError("COCO json中没有 images 字段或 images 为空")

    if not categories:
        raise ValueError("COCO json中没有 categories 字段或 categories 为空")

    # 建立 category_id 到 YOLO class_id 的映射
    # 注意：COCO中的category_id可能不是从0开始，也可能不连续
    # YOLO要求类别编号从0开始且连续
    categories = sorted(categories, key=lambda x: x["id"])

    category_id_to_yolo_id = {}
    yolo_id_to_name = {}

    for yolo_id, cat in enumerate(categories):
        coco_cat_id = cat["id"]
        cat_name = cat.get("name", str(coco_cat_id))

        category_id_to_yolo_id[coco_cat_id] = yolo_id
        yolo_id_to_name[yolo_id] = cat_name

    # 保存类别名称
    if save_classes_txt:
        classes_path = output_labels_dir / "classes.txt"
        with open(classes_path, "w", encoding="utf-8") as f:
            for yolo_id in range(len(yolo_id_to_name)):
                f.write(yolo_id_to_name[yolo_id] + "\n")

        print(f"类别文件已保存: {classes_path}")

    # 建立 image_id 到 image_info 的映射
    image_id_to_info = {}
    for img in images:
        image_id_to_info[img["id"]] = img

    # 建立 image_id 到 annotation列表 的映射
    image_id_to_annotations = {}
    for ann in annotations:
        image_id = ann["image_id"]
        image_id_to_annotations.setdefault(image_id, []).append(ann)

    converted_box_count = 0
    skipped_box_count = 0

    # 遍历每张图片，生成对应txt
    for image_id, img_info in image_id_to_info.items():
        file_name = img_info["file_name"]
        img_width = img_info["width"]
        img_height = img_info["height"]

        image_stem = Path(file_name).stem
        txt_path = output_labels_dir / f"{image_stem}.txt"

        anns = image_id_to_annotations.get(image_id, [])

        yolo_lines = []

        for ann in anns:
            # 如果是 crowd 标注，可以选择跳过
            if ann.get("iscrowd", 0) == 1:
                skipped_box_count += 1
                continue

            category_id = ann["category_id"]

            if category_id not in category_id_to_yolo_id:
                print(f"警告: category_id={category_id} 不在 categories 中，跳过")
                skipped_box_count += 1
                continue

            yolo_class_id = category_id_to_yolo_id[category_id]

            bbox = ann.get("bbox", None)
            if bbox is None or len(bbox) != 4:
                print(f"警告: image_id={image_id} 中存在无效bbox，跳过")
                skipped_box_count += 1
                continue

            # COCO bbox: [x_min, y_min, width, height]
            x_min, y_min, box_width, box_height = bbox

            # 过滤无效框
            if box_width <= 0 or box_height <= 0:
                skipped_box_count += 1
                continue

            # 转换为 YOLO 格式，归一化
            x_center = x_min + box_width / 2
            y_center = y_min + box_height / 2

            x_center_norm = x_center / img_width
            y_center_norm = y_center / img_height
            width_norm = box_width / img_width
            height_norm = box_height / img_height

            # 防止极少数标注越界
            x_center_norm = min(max(x_center_norm, 0), 1)
            y_center_norm = min(max(y_center_norm, 0), 1)
            width_norm = min(max(width_norm, 0), 1)
            height_norm = min(max(height_norm, 0), 1)

            yolo_line = (
                f"{yolo_class_id} "
                f"{x_center_norm:.6f} "
                f"{y_center_norm:.6f} "
                f"{width_norm:.6f} "
                f"{height_norm:.6f}"
            )

            yolo_lines.append(yolo_line)
            converted_box_count += 1

        # 写入txt
        # 如果该图像没有标注，根据 create_empty_txt 决定是否创建空txt
        if yolo_lines or create_empty_txt:
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write("\n".join(yolo_lines))

    print("\n转换完成！")
    print(f"图像数量: {len(images)}")
    print(f"标注数量: {len(annotations)}")
    print(f"成功转换bbox数量: {converted_box_count}")
    print(f"跳过bbox数量: {skipped_box_count}")
    print(f"YOLO标签保存目录: {output_labels_dir}")


if __name__ == "__main__":
    coco_json_path = r"train_1.json"
    output_labels_dir = r"dota_labels"

    coco_to_yolo(
        coco_json_path=coco_json_path,
        output_labels_dir=output_labels_dir,
        save_classes_txt=True,
        create_empty_txt=True
    )