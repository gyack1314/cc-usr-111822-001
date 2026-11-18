# 显示面板质检与结算

项目按来源版本保存业务资料，已有 production、inspection、settlement 环节。现有生产、检验和结算只处理单批次资料，尚不能区分 AI 上线与供应商、产品结构和停机共同变化。

运行与检查：

    python -m unittest discover -s tests -v
    python -m compileall -q panel_ops tests
    python -m panel_ops.cli data/example.json
