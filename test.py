from matplotlib import pyplot as plt
from a import selective_serach as rpn
from mindvision.classification.models import resnet50
import mindspore as ms

net = resnet50(pretrained=True)
image = plt.imread("/home/xw/xw/Heavy/datasets/coco_dataset_dir/train2017/000000082835.jpg")
output = net(ms.Tensor(image, ms.float32))

# image, region_proposal = rpn.selective_search(im_orig=image)
# print(region_proposal)
# plt.figure(figsize=(10, 10))
# plt.imshow(image)
# plt.show()


