---
theme: @eastgold15/slidev-theme-jingjiang
title: 体育学院2024年工作总结
---

# 体育学院

述职PPT

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" flex="~ justify-center items-center gap-2" hover="bg-white bg-opacity-10">
    Press Space for next page <div class="i-carbon:arrow-right inline-block" />
  </span>
</div>

---

layout: cover

# 体育学院2024年度工作总结

述职汇报

<div class="cover-divider"></div>

<div class="cover-footer">
  <span>体育学院</span>
  <span>2024年12月</span>
</div>

---

layout: circletl-br

# 目录 CONTENTS

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

### 01 工作概述
关键数据指标一览

### 02 专业建设
学科布局与数据成果

</div>

<div>

### 03 重点项目
年度标志性工作推进

### 04 展望规划
未来工作方向与目标

</div>

</div>

---

layout: circletr-bl

# 工作概述

## 2024年体育学院核心数据指标

<div class="grid grid-cols-3 gap-6 mt-6">

<Card title="在校生规模" accent="#F9D240">
  <div class="text-center py-4">
    <div class="text-5xl font-bold text-data">1,286</div>
    <div class="text-desc text-sm mt-2">同比增长 8.3%</div>
  </div>
</Card>

<Card title="专业数量" accent="#F9D240">
  <div class="text-center py-4">
    <div class="text-5xl font-bold text-data">6</div>
    <div class="text-desc text-sm mt-2">本科专业 + 2 个方向</div>
  </div>
</Card>

<Card title="就业率" accent="#F9D240">
  <div class="text-center py-4">
    <div class="text-5xl font-bold text-data">92.7%</div>
    <div class="text-desc text-sm mt-2">较去年提升 4.1%</div>
  </div>
</Card>

</div>

<div class="grid grid-cols-3 gap-6 mt-6">

<Card title="科研项目" accent="#F9D240">
  <div class="text-center py-4">
    <div class="text-5xl font-bold text-data">18</div>
    <div class="text-desc text-sm mt-2">省部级立项 7 项</div>
  </div>
</Card>

<Card title="竞赛获奖" accent="#F9D240">
  <div class="text-center py-4">
    <div class="text-5xl font-bold text-data">43</div>
    <div class="text-desc text-sm mt-2">国家级奖项 11 项</div>
  </div>
</Card>

<Card title="师资队伍" accent="#F9D240">
  <div class="text-center py-4">
    <div class="text-5xl font-bold text-data">89</div>
    <div class="text-desc text-sm mt-2">高级职称占比 42.7%</div>
  </div>
</Card>

</div>

---

# 专业建设数据

## 2024年度各专业基本情况一览

<ScrollView max-height="380px">

| 专业名称 | 年级 | 在校人数 | 就业率 | 备注 |
| :--- | :--- | :---: | :---: | :--- |
| 体育教育 | 2021-2024 | 486 | 93.5% | 师范类专业认证已通过 |
| 运动训练 | 2021-2024 | 312 | 91.2% | 省一流专业建设点 |
| 社会体育指导与管理 | 2021-2024 | 208 | 90.8% | 新增休闲体育方向 |
| 武术与民族传统体育 | 2022-2024 | 126 | 94.1% | 校重点特色专业 |
| 运动人体科学 | 2021-2024 | 89 | 89.7% | 今年恢复招生 |
| 休闲体育 | 2023-2024 | 65 | — | 2023年新增专业 |
| <span class="text-total">合计</span> | <span class="text-total">—</span> | <span class="text-total">1,286</span> | <span class="text-total">92.7%</span> | — |

</ScrollView>

<div class="card-full-width mt-4 p-4 flex items-center gap-4">
  <span class="text-lg font-bold">专业建设成效：</span>
  <span class="text-desc">体育教育专业通过师范类专业认证，运动训练专业获批省一流专业建设点，新增休闲体育专业并完成首次招生。</span>
</div>

---

# 重点项目

## 2024年度重大工作推进情况

<MermaidView :max-height="420">

```mermaid
graph TB
    Start(("体育学院<br/>2024年重点项目")) --> A["师范类专业认证"]
    Start --> B["省一流专业建设"]
    Start --> C["学科竞赛体系建设"]
    Start --> D["师资引培计划"]

    A --> A1["完成体育教育专业<br/>师范类二级认证"]
    A --> A2["修订人才培养方案<br/>强化教学实践环节"]
    A1 --> A3{"认证结论"}
    A2 --> A3
    A3 -->|"通过"| A4["获批教师资格<br/>免试认定资格"]

    B --> B1["运动训练专业<br/>省一流建设点获批"]
    B --> B2["建设期内完成<br/>5项关键指标"]
    B1 --> B3["获专项建设<br/>经费 80 万元"]

    C --> C1["全年参赛 25 项<br/>获得国家级奖 11 项"]
    C --> C2["省级奖 32 项<br/>创历年最好成绩"]
    C1 --> C3["建立竞赛专项<br/>经费保障机制"]

    D --> D1["引进博士 4 人<br/>硕士 6 人"]
    D --> D2["选派 8 名教师<br/>出国访学研修"]
    D1 --> D3["高级职称教师<br/>占比提升至 42.7%"]

    style Start fill:#4C2668,stroke:#9D78C2,stroke-width:2px,color:#fff
    style A fill:#532B73,stroke:#9D78C2,color:#fff
    style B fill:#532B73,stroke:#9D78C2,color:#fff
    style C fill:#532B73,stroke:#9D78C2,color:#fff
    style D fill:#532B73,stroke:#9D78C2,color:#fff
    style A3 fill:#42205C,stroke:#F9D240,stroke-width:2px,color:#F9D240
    style A4 fill:#4C2668,stroke:#F9D240,color:#F9D240
    style B3 fill:#4C2668,stroke:#F9D240,color:#F9D240
    style C3 fill:#4C2668,stroke:#F9D240,color:#F9D240
    style D3 fill:#4C2668,stroke:#F9D240,color:#F9D240
```

</MermaidView>

---

layout: circletl-br

# 展望规划

## 2025年度重点工作方向

<div class="grid grid-cols-2 gap-6 mt-6">

<Card title="深化专业内涵建设" :show-accent="true" accent="#F9D240">
  <ul class="text-desc space-y-2 mt-2">
    <li>推进运动训练专业省一流验收</li>
    <li>启动社会体育指导与管理专业认证</li>
    <li>申报运动康复新专业</li>
  </ul>
</Card>

<Card title="提升科研创新能力" :show-accent="true" accent="#F9D240">
  <ul class="text-desc space-y-2 mt-2">
    <li>力争国家级课题立项 2-3 项</li>
    <li>建设校级体育科学重点实验室</li>
    <li>推动跨学科交叉研究平台落地</li>
  </ul>
</Card>

<Card title="优化师资队伍结构" :show-accent="true" accent="#F9D240">
  <ul class="text-desc space-y-2 mt-2">
    <li>引进高层次人才 5-8 人</li>
    <li>培育省级教学名师 1-2 人</li>
    <li>完善青年教师导师制培养体系</li>
  </ul>
</Card>

<Card title="拓展社会服务能力" :show-accent="true" accent="#F9D240">
  <ul class="text-desc space-y-2 mt-2">
    <li>建设全民健身志愿服务品牌</li>
    <li>深化校地合作体育培训项目</li>
    <li>打造区域体育赛事服务中心</li>
  </ul>
</Card>

</div>

---

layout: cover

# 感谢聆听

## 恳请各位领导批评指正

<div class="cover-divider"></div>

<div class="cover-footer">
  <span>体育学院</span>
  <span>2024年12月</span>
</div>
