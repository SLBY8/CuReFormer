import os
import sys
import json
import cv2
import argparse
import numpy as np

sys.path.append('./')

from engine.deim.utils import DensityMapGenerator, visualize_density_map


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--image',
        '-i',
        default=r"E:\\DEIM_2938868228\\DOTA_split\\trainsplit\\images\\P2014__1__1648___824.jpg",
        type=str,
        help='单张图片路径'
    )

    parser.add_argument(
        '--json',
        '-j',
        default=r"E:\\DEIM_2938868228\\DOTA_split\\annotations\\train.json",
        type=str,
        help='COCO格式标注json路径'
    )

    parser.add_argument(
        '--save_path',
        '-s',
        default='DensityMap_val_1',
        type=str,
        help='保存结果的文件夹'
    )

    args = parser.parse_args()

    os.makedirs(args.save_path, exist_ok=True)

    # 读取图片
    image = cv2.imread(args.image)
    if image is None:
        raise FileNotFoundError(f"图片读取失败: {args.image}")

    image_name = os.path.basename(args.image)

    # 读取 COCO json
    with open(args.json, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 找到当前图片对应的 image_id
    target_image_id = None
    target_height = None
    target_width = None

    for image_data in data['images']:
        if image_data['file_name'] == image_name:
            target_image_id = image_data['id']
            target_height = int(image_data['height'])
            target_width = int(image_data['width'])
            break

    if target_image_id is None:
        raise ValueError(f"在 JSON 中没有找到图片: {image_name}")

    # 收集该图片的 bbox
    boxes = []

    for box_data in data['annotations']:
        if box_data['image_id'] == target_image_id:
            box = np.array(box_data['bbox'], dtype=np.float32)

            # COCO bbox: [x_min, y_min, w, h]
            # 转成 [x_center, y_center, w, h]
            box[:2] = box[:2] + box[2:] / 2

            boxes.append(box)

    boxes = np.array(boxes, dtype=np.float32)

    # 防止没有标注时报错
    if len(boxes) == 0:
        boxes = np.zeros((0, 4), dtype=np.float32)

    # 注意这里 height 和 width 必须是 int
    dmg = DensityMapGenerator([target_height, target_width])

    densitymap = dmg.generate_from_boxes(boxes, method='gaussian')

    save_file = os.path.join(args.save_path, image_name)

    visualize_density_map(
        image,
        densitymap,
        boxes,
        save_file
    )

    print(f"完成: {save_file}")
    print(f"图片: {image_name}")
    print(f"image_id: {target_image_id}")
    print(f"标注框数量: {len(boxes)}")


if __name__ == '__main__':
    main()