> 发布说明：此文件保留 2026-09-24 原始交接内容；“本次”均指当时工作。模型、审查预览图与旧表单独备份未随公开仓库提供。当前发布状态见仓库首页。

# pets — Pet Assets × Gene Table v2（扩充草案）

更新：2026-09-24。本版对应实际目录 `new model（本地资产源目录，未随仓库提供）` 的 13 个 GLB。

**阅读顺序：第 1–6 节是本次实测与建议扩展；后半部完整保留 2026-09-23 旧表作为历史依据，不代表旧代码今天仍如此。**

- **已确认**：文件存在、SHA-256、面数、包围盒、材质/贴图/动画计数来自本次 GLB 解析；13 个全无骨骼 skin 和动画。
- **建议**：角色命名、基因语义、初代纯合、显隐关系、表达规则；不能从 3D 资产推断隐性基因。
- **待确认**：Fenxiang 名称与外观、旧 8 项与新 13 项是否重复/替代、运行时尺寸、游戏加载与性能。旧表的 8 项未在本次目录重测，不能宣称已有 21 个独立物种。
- **未做**：未改动游戏代码、未发起收费 Tripo 任务、未新生成杂交 GLB。

配套：`基因重组实现方案.md`、`gene_assets_v2.json`、`asset_inventory.json`、`recombination_reference.py`、`simulation_report.json`。

## 1. new model 当前资产清单（实测）

X×Y×Z 为文件坐标的包围盒，不代表米数/物理体型/游戏战力。图片数指 GLB 内图片数量，可能包括 baseColor、法线和 roughness，而不是参考照片数量。网格多也不证明可直接拼装。

| ID | 角色 | GLB | 三角面 | X×Y×Z 包围盒 | 图片/网格数 | 识别锚点 |
|---|---|---|---:|---|---|---|
| `pink-dog` | 粉耳奶白狗球 | `Character_Fengou_P1_Face3000_Jelly.glb` | 3,026 | 0.885×0.943×0.998 | 3 / 1 | 大黑眼＋奶白短口鼻；粉色垂耳和蓬松头毛 |
| `pink-droop` | 粉色垂耳猪鼻球（身份待确认） | `Character_Fenxiang_P1_Face3000_Jelly.glb` | 2,931 | 0.854×0.752×0.998 | 3 / 1 | 半闭困倦眼＋双鼻孔短猪鼻＋长垂耳 |
| `curious-cat` | 好奇虎斑猫球 | `Character_Haoqimao_P1_Face3000_Jelly.glb` | 2,825 | 0.982×0.998×0.990 | 3 / 1 | 黄绿色大眼＋粉三角鼻＋额头虎斑＋白口鼻 |
| `teddy` | 皱眉泰迪熊球 | `Character_Taidixiong_P1_Face3000_Jelly.glb` | 2,964 | 0.998×0.955×0.979 | 3 / 1 | 皱眉压眼＋奶白宽口鼻＋小黑鼻＋圆耳 |
| `black-cat` | 罗小黑式黑猫球 | `Character_luoxiaohei_Jelly.glb` | 2,982 | 0.998×0.846×0.979 | 3 / 1 | 巨椭圆白眼黑瞳＋小嘴＋尖耳＋球尾 |
| `reborn` | 帽子火焰宝宝球 | `Character_reborn.glb` | 2,836 | 0.982×0.998×0.998 | 3 / 1 | 大眼宝宝脸＋黑礼帽橙帽带＋额前火焰＋绿小动物装饰 |
| `heart-emoji` | 爱心红晕黄豆 | `ahegao.glb` | 6,984 | 1.960×1.960×2.039 | 0 / 34 | 爱心瞳孔＋大湿眼＋鼻脸红晕＋波浪嘴＋泪痕 |
| `banana-cat` | 香蕉猫 | `banana_cat.glb` | 2,272 | 1.336×2.553×0.835 | 1 / 16 | 猫脸正前方＋弯香蕉轮廓＋深色棱线＋短手脚 |
| `sad-frog` | 球面悲伤蛙半身像 | `beishangwa.glb` | 4,160 | 1.720×1.950×1.603 | 0 / 23 | 大白眼垂眼皮＋棕厚唇＋眼下褶线＋蓝上衣 |
| `knife-dog` | 粉发刀盾小狗 | `daodunaniya.glb` | 5,894 | 3.549×2.470×1.855 | 0 / 64 | 犬鼻口微笑＋粉中分短发呆毛＋黑金耳饰＋刀盾 |
| `fengge` | 黄躯卷发胡子兽 | `fengge.glb` | 2,952 | 2.188×2.368×2.696 | 0 / 45 | 圆胖趴卧＋凸圆眼＋中长卷发＋八字胡山羊胡 |
| `gentle-penguin` | 高雅读报企鹅 | `gaoyarenshi.glb` | 4,648 | 1.919×2.445×1.440 | 0 / 159 | 黑白分区＋黄鸟喙＋粗框墨镜＋捧报姿势 |
| `lip-chicken` | 红唇人鱼鸡 | `renyuji.glb` | 4,780 | 1.661×2.431×1.139 | 1 / 39 | 上置大眼紫睫毛＋橙腮红＋蓝绿嘴周＋红厚唇＋细鸡脚 |

### 入库要点

1. 六个 `Character_*` 文件都是单网格、3 张内嵌图片，alpha=0.95、BLEND、基础 roughness=0.18，另有材质纹理；未声明 `KHR_materials_transmission`。不能把文件名 Jelly 当“果冻”已实现场景效果。
2. 六个单网格样本的三向预览显示正脸朝文件 +X；其他本会话生成文件按 +Z 正面约定。统一正面轴前先预览核对，不能只凭 glTF 的 Y-up 认为都同向。
3. `ahegao.glb` 是爱心红晕黄豆，`beishangwa.glb` 是圆鼓半身蛙。主体球体应检查身体网格，不以整个带嘴唇/泪滴的包围盒严格相等判断。
4. `daodunaniya.glb` 有 5894 面；它与旧表 `pet_knife_shiba.glb` 的 324 面文件不同，不应沿用旧面数或默认为同一版本。
5. `Character_Fenxiang...` 可见长垂耳、困眼和双孔短猪鼻，并非明显象鼻。暂记“粉色垂耳猪鼻球”，身份待确认。
6. `renyuji.glb` 的嘴周和身体用了参考图纹理；`banana_cat.glb` 猫脸用了原图。照片有条纹/低清的缺陷不应遗传为“生物基因”。
7. 当前目录没有西装老头、牛、蓝球、流汗黄豆和粉色眨眼角色。聊天里曾制作过不等于本目录已收录。先标候选，确认文件/版本再启用。

## 2. 新资产的主要性状（v2 建议标签）

本表是可见性状，不是隐性基因检测结果。`none` 只用于确认的缺省部件；尚不能确认的特征应标 unknown 并禁止自动入池。

| ID | 体型 body_plan | 脸包 face_pack | 体色 body_color | 表面 surface | 耳朵 ear_pack | 头发 hair_pack / hair_color | 胡子 beard_pack |
|---|---|---|---|---|---|---|---|
| `pink-dog` | round_quadruped | dog_big_eyes | cream | fur | floppy_pink | pink_cream_fluff / pink | none |
| `pink-droop` | round_stub_feet | sleepy_pig_snout | pink | smooth | long_droop | none / none | none |
| `curious-cat` | round_quadruped | curious_tabby | tabby_brown_cream | fur | cat_pointed | none / none | none |
| `teddy` | round_stub_feet | frowning_bear | tan | fur | bear_round | none / none | none |
| `black-cat` | round_cat_blob | black_cat_oval_eyes | black | smooth | cat_pointed | none / none | none |
| `reborn` | round_stub_feet | baby_round_eyes | peach | smooth | none | none / none | none |
| `heart-emoji` | sphere | heart_blush_tears | yellow | smooth | none | none / none | none |
| `banana-cat` | banana_upright | photo_kitten | banana_yellow | peel | none | none / none | none |
| `sad-frog` | round_bust | sad_frog | green | smooth | none | none / none | none |
| `knife-dog` | round_stub_feet | smirking_dog_blush | pink_cream | smooth | none | pink_bob_tuft / pink | none |
| `fengge` | prone_quadruped | bulging_eyes_moustache | yellow | smooth | none | medium_wavy / black | moustache_goatee |
| `gentle-penguin` | penguin_upright | penguin_beak | black_white | smooth | none | none / none | none |
| `lip-chicken` | egg_biped | lip_chicken | pale_yellow | mottled_reference | none | none / none | none |

| ID | 头饰 headwear | 眼镜 eyewear | 衣服 outfit | 手持 handheld | 尾 tail | 翼/鳍 wing | 发光/火焰形态 glow |
|---|---|---|---|---|---|---|---|
| `pink-dog` | none | none | none | none | short_curled | none | none |
| `pink-droop` | none | none | none | none | none | none | none |
| `curious-cat` | none | none | red_collar | none | cat_curled | none | none |
| `teddy` | none | none | none | none | bear_stub | none | none |
| `black-cat` | none | none | none | none | cat_ball_tip | none | none |
| `reborn` | black_fedora_orange_band | none | black_high_collar | none | none | none | hat_flame |
| `heart-emoji` | none | none | none | none | none | none | none |
| `banana-cat` | banana_stalk | none | none | none | none | none | none |
| `sad-frog` | none | none | blue_shirt | none | none | none | none |
| `knife-dog` | black_gold_cones | none | none | knife_shield | none | none | none |
| `fengge` | none | none | none | none | none | none | none |
| `gentle-penguin` | none | thick_sunglasses | none | newspaper | none | flippers | none |
| `lip-chicken` | orange_comb | none | none | none | none | small_wings | none |

`glow=hat_flame` 目前只代表可见火焰装饰的建议语义；真实自发光/照明未确认，不得自动赋战斗或灯光效果。`surface=fur` 依据毛感纹理判定，不代表有实体毛发。`pink_cream_fluff` 是狗的头顶绒毛，不代表人类发型。

其余建议默认：`horn_pack=none`、`body_scale=A`（游戏待统一，不是实测）、`hand_scale=normal`、`claw=none`、`limb_color=inherit_body`、`back=none`。它们只用于初代草案；未知隐藏等位基因不自动填“红色/第一形态”。

### 角色不能丢掉的识别锚点与证据边界

- **粉耳奶白狗球**：大黑眼＋奶白短口鼻；粉色垂耳和蓬松头毛。注意：耳朵是粉耳，不能迁移成粉色人类头发；命名粉狗为暂定展示名。
- **粉色垂耳猪鼻球（身份待确认）**：半闭困倦眼＋双鼻孔短猪鼻＋长垂耳。注意：文件名 Fenxiang，实物不是明显长象鼻；不要未经确认写成粉象。
- **好奇虎斑猫球**：黄绿色大眼＋粉三角鼻＋额头虎斑＋白口鼻。注意：红项圈和虎斑属于区域纹样；不能全身单色染掉。
- **皱眉泰迪熊球**：皱眉压眼＋奶白宽口鼻＋小黑鼻＋圆耳。注意：毛感主要来自贴图；不是要逐根建毛。
- **罗小黑式黑猫球**：巨椭圆白眼黑瞳＋小嘴＋尖耳＋球尾。注意：保留浅绿耳内和白眼，黑底色只改指定区域。
- **帽子火焰宝宝球**：大眼宝宝脸＋黑礼帽橙帽带＋额前火焰＋绿小动物装饰。注意：礼帽与火焰要占不同锚点；本地材质并未证明火焰有真实发光。
- **爱心红晕黄豆**：爱心瞳孔＋大湿眼＋鼻脸红晕＋波浪嘴＋泪痕。注意：已读到球体修正版；主体球面与整模包围盒区分，泪滴等会超出主体。
- **香蕉猫**：猫脸正前方＋弯香蕉轮廓＋深色棱线＋短手脚。注意：原图脸部纹理有横纹；香蕉壳颜色和猫脸纹理必须分区。
- **球面悲伤蛙半身像**：大白眼垂眼皮＋棕厚唇＋眼下褶线＋蓝上衣。注意：是半身像，没有腿；如游戏要腿，应单列体型适配而非宣称原模型有。
- **粉发刀盾小狗**：犬鼻口微笑＋粉中分短发呆毛＋黑金耳饰＋刀盾。注意：目前为纯色低模；预期毛感不等于实际带毛纹理，黑金锥饰不算生物牛角。
- **黄躯卷发胡子兽**：圆胖趴卧＋凸圆眼＋中长卷发＋八字胡山羊胡。注意：眼睛/脸可迁移；胡子不与嘴唇随机拼坏。
- **高雅读报企鹅**：黑白分区＋黄鸟喙＋粗框墨镜＋捧报姿势。注意：墨镜遮盖眼睛不等于无眼睛；原图特征保留但可改身体色区域。
- **红唇人鱼鸡**：上置大眼紫睫毛＋橙腮红＋蓝绿嘴周＋红厚唇＋细鸡脚。注意：贴图来自低清参考局部；身形不像时不能单凭有纹理算通过。

## 3. v2 与旧 32 槽的兼容办法

旧数组索引、原选项顺序不动。v2 是权威数据；兼容器仅派生旧数组和 `unmappedTraits`。任何不能表示的性状不可硬塞到错误选项，例如把火焰当机器指示灯、把香蕉当普通哺乳动物、把黑金耳饰当牛角。

| 旧槽 | v2 来源 | 处理 |
|---|---|---|
| 1 skeleton | 资产骨骼配置 | noSkeleton 为技术元数据，不参与性状重组；保留占位索引 |
| 2 body | body_scale | A 等级暂作迁移默认；S 单独讨论，不能重排旧6项 |
| 3 bodyColor | body_color 的身体底色区域 | 单色可映射；双色/虎斑记 unmapped，不能丢 v2 原值 |
| 4 bodyTex | surface | smooth/fur 可映射；peel/mottled 为新语义；半透明渲染配置另存 |
| 5 bodyForm | body_plan | sphere 可映射；round_bust/banana 等需扩展或兼容占位并标损失，不伪称原生支持 |
| 6–8 eyeOn/Color/Form | face_pack 内的眼睛定义 | 遮挡不等于无眼；爱心瞳孔等写扩展字段，旧 form=emoji 只作粗略投影 |
| 9–11 ear | ear_pack | none 关闭；内部颜色/形态保存在 pack |
| 12–14 horn | horn_pack | 独立于 headwear，不把帽子发夹塞进牛角 |
| 15–17 wing | wing | small_wings 可粗映 feather；flippers 标 unmapped，避免长出飞行羽翼 |
| 18–20 tail | tail | 球尾和弯猫尾细节保存在 pack；旧表只表达兽尾大类 |
| 21–23 back | back | none 关闭，未观察到的结构不补造 |
| 24–26 limb | body_plan 内的 limb layout | 半身蛙/球体按真实体型处理；“要能战斗”不能推导出应有四腿 |
| 27–29 claw | claw + hand_scale | giant_index 不是 giant claw；必须走扩展字段 |
| 30–32 glow | glow + 材质证据 | 火焰形状不自动代表真实发光；无法兼容则 unmapped |

旧数组只有一个 phenotype 选项索引，不能装下 `[A,a]`。升级时将旧值迁到两份相同等位基因；旧的 `latent*` 若有真实策划配置可保留，但若只是第一项占位，应记 `legacy_placeholder`、待审核，**不当成已设计的隐性基因**。

建议增加到保存记录而非简单插入 32 数组：`schemaVersion`、`genomeV2`、`phenotypeV2`、`suppressedTraits`、`rulesVersion`、`parentIds`、`generationSeed`、`assetId`。存档可保留 `genomeLegacy32` 只读快照。

## 4. 显性 / 隐性 / 不表达（简版约定）

- 每个位点两个等位基因；每个父母各贡献一个。**遗传抽样与显性表达是两个步骤。**
- 显隐对按位点配置，不给全角色排统一强弱。
- 互斥不同等位基因无显隐对时，固定种子选择一个表达；本次结果存档。
- 表情是连锁脸包；发型/发色同源传递；体型/比例同源传递。
- `none/none` 为缺省；被另一个等位基因盖住、因缺锚点不表达、因遮挡/预算不表达须分别记录。
- 隐性或被抑制的基因仍遗传。普通隐藏不应该全被 UI 称为“隐性”。
- 一个主体、一个主脸包、最多两个额外高显著借入特征。不是所有 21 个位点都各长出一个部件。
- 初代建议已观察值 X/X；想加入隐藏基因应由策划明确配置，不从 GLB 猜测。

详细流程和约束见 `基因重组实现方案.md`。默认显隐参数尚为草案；不能由这次统计推导出角色属性、稀有度或战斗值。

## 5. 待入库候选（不参与当前自动繁殖）

| 候选 | 目的 | 还缺什么 |
|---|---|---|
| 冷淡牛 / bull-aloof | 牛角、牛鼻、绿色牛哈黄豆组合的牛身份来源 | 从旧资产库读取真实 GLB；核对面数、鼻角和身体 |
| 肥胖无脖子西装老头 | stocky_no_neck_chibi＋wide_open_mouth_man＋suit＋giant_index | 本次目录无该文件；须选正确无脖子修订版 |
| 红发色等位基因 | 红头发西装老头 | 当前新资产无红人类头发；指定祖代或受控变异，不能凭空重组产生 |
| 流汗黄豆 / 蓝色球体 | sweat_drop / sleepy_pout 等脸包 | 选择版本并入库；蓝球原图无墨镜，需要区分变体 |
| 粉色眨眼角色 | wink＋花＋门牙 | 选择最终 GLB，验证是否还要毛感纹理 |

## 6. 当前验证结论

- 13 个文件结构可读、统计完成；单网格六项已渲染三方向检视，预览不模拟完整 PBR 和透明排序，不能用来证明果冻效果。
- 本次只是资产盘点与遗传原型，不是发布环境性能验收。
- `recombination_reference.py` 的离线测试通过：同种子确定、父母顺序无关、每亲本各取一条、隐藏携带不丢失；4096 次二代绿色出现 1077 次（26.29%）。
- Tripo 接入文档已核对；本次没有真实任务提交/扣费/模型神似验收。

---

# 历史附件：2026-09-23 原始基因表（原文保留）

以下内容不因保留而变成今天已重新核验的运行状态。

# pets — Pet Assets x Gene Table

Date: 2026-09-23
Source of the gene table: `DESIGN-genes.md` (user's table, normalized to 32 slots) and `GENE_DEFS` in `index.html`.
All names are English / pinyin only. `genome[i]` = option index of slot `i` (0-based), same order as `GENE_DEFS`.

---

## 1. Asset roster — final version per pet

| # | key | English name | CN name | file | tris | raw size (w x h x d, unit) | in-game size | status |
|---|---|---|---|---|---|---|---|---|
| 1 | slime-ring | Ring Slime | 浮环史莱姆 | `pet_slime_ring.glb` | 4959 | 0.795 x 0.979 x 0.998 | A box 1.488 x 1.832 x 1.869 m | in game (count 20) |
| 2 | slime-ball | Sticky Blob Slime | 粘球史莱姆 | `pet_slime_ball.glb` | 4840 | 0.998 x 0.721 x 0.834 | A box (same as above) | in game (count 20) |
| 3 | knife-shiba | Knife-Shield Shiba Ball | 持刀盾柴犬球 | `pet_knife_shiba.glb` | 324 | 0.713 x 0.877 x 0.998 | currently box **S** 1.136 x 1.408 x 1.600 m | in game (count 10) |
| 4 | kangaroo-peek | Peeking Kangaroo | P-01 偷偷看袋鼠 | `pet_kangaroo_peek.glb` | 4746 | 0.998 x 0.998 x 0.881 | not in game yet | asset ready |
| 5 | bull-aloof | Aloof Bull | P-03 冷淡牛 | `pet_bull_aloof.glb` | 4894 | 0.971 x 0.826 x 0.998 | not in game yet | asset ready |
| 6 | baby-laugh | Belly-Laugh Baby | P-04 捧腹大笑奶娃 | `pet_baby_laugh.glb` | 5014 | 0.998 x 0.994 x 0.994 | not in game yet | asset ready |
| 7 | sunny-sun | Sunny the Sun | 太阳 Sunny | `pet_sunny_sun.glb` | 2817 | 0.318 x 0.998 x 0.920 | not in game yet | asset ready |
| 8 | mind-sphere | Mind Probe Sphere | C-01 心灵探测球 | `pet_mind_sphere.glb` | 2988 | 0.514 x 0.998 x 0.568 | not in game yet | asset ready |

### Variants (`variants/`)

| file | tris | note |
|---|---|---|
| `pet_knife_shiba_lod0.glb` | 60 | minimum-face LOD of the shiba |
| `pet_sunny_sun_singleview.glb` | 2864 | single-view jelly build |
| `pet_sunny_sun_singleview_v2.glb` | 2864 | single-view, softer depth fix |
| `pet_sunny_sun_raw.glb` | 4775 | original P1 output, no face limit |
| `pet_mind_sphere_head.glb` | 1632 | head only, cut at the neck |

Machine-readable version of everything below: `pets.json`.

---

## 2. The 32 gene slots (English)

Color slots always use this 13-step palette:
`red, yellow, blue, green, purple, light red, light yellow, light blue, light green, light purple, gray, black, white`

| n | key | English label | options |
|---|---|---|---|
| 1 | skeleton | Skeleton | no skeleton points |
| 2 | body | Body size | same as slime-ring / 40% bigger / 80% bigger / 120% bigger / width+depth 80% bigger (height same) / height 80% bigger (width+depth same) |
| 3 | bodyColor | Body color | 13 colors |
| 4 | bodyTex | Body texture | smooth / slimy / rough / jelly / crystal / metal / furry / shell |
| 5 | bodyForm | Body form | sphere / naiLong / standard mammal / slime shape |
| 6 | eyeOn | Eyes present | yes / no |
| 7 | eyeColor | Eye color | 13 colors |
| 8 | eyeForm | Eye form | animal eye / machine eye / snail eye / emoji eye |
| 9 | earOn | Ears present | yes / no |
| 10 | earColor | Ear color | 13 colors |
| 11 | earForm | Ear form | animal ear / machine ear / emoji ear / elf ear |
| 12 | hornOn | Horn/crown present | yes / no |
| 13 | hornColor | Horn/crown color | 13 colors |
| 14 | hornForm | Horn/crown form | sheep horn / bull horn / unicorn / crown / helmet / machine antenna *(source table skips E — only 6 options)* |
| 15 | wingOn | Wings present | yes / no |
| 16 | wingColor | Wing color | 13 colors |
| 17 | wingForm | Wing form | feather wing / pterosaur wing / propeller |
| 18 | tailOn | Tail present | yes / no |
| 19 | tailColor | Tail color | 13 colors |
| 20 | tailForm | Tail form | beast tail / dinosaur tail / fish tail / machine tail |
| 21 | backOn | Back feature present | yes / no |
| 22 | backColor | Back feature color | 13 colors |
| 23 | backForm | Back feature form | dragon fin / sword bone / back machine gun / backpack |
| 24 | limbOn | Limbs present | yes / no |
| 25 | limbColor | Limb color | 13 colors |
| 26 | limbForm | Limb form | standard small animal / standard big animal |
| 27 | clawOn | Claws present | yes / no |
| 28 | clawColor | Claw color | 13 colors |
| 29 | clawForm | Claw form | sharp / giant |
| 30 | glowOn | Glow organ present | yes / no |
| 31 | glowColor | Glow organ color | 13 colors |
| 32 | glowForm | Glow organ form | anglerfish lure / machine indicator |

---

## 3. Genome matrix (8 pets x 32 slots)

Rows = gene slots, columns = pets. `A/B/...` = body-size grade; `yes/no` = presence only where relevant.

| n | gene | ring | ball | shiba | kangaroo | bull | baby | sunny | mind |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Skeleton | noSkeleton | noSkeleton | noSkeleton | noSkeleton | noSkeleton | noSkeleton | noSkeleton | noSkeleton |
| 2 | Body size | A | A | A | A | A | A | A | A |
| 3 | Body color | light yellow | light blue | yellow | yellow | yellow | yellow | yellow | light red |
| 4 | Body texture | jelly | jelly | furry | furry | furry | smooth | jelly | smooth |
| 5 | Body form | sphere | sphere | sphere | standard mammal | standard mammal | standard mammal | sphere | sphere |
| 6 | Eyes present | no | no | yes | yes | yes | yes | yes | yes |
| 7 | Eye color | light yellow* | light blue* | yellow | yellow | yellow | yellow | yellow | light red |
| 8 | Eye form | animal* | animal* | animal eye | emoji eye | animal eye | emoji eye | emoji eye | animal eye |
| 9 | Ears present | no | no | yes | yes | yes | yes | no | no |
| 10 | Ear color | light yellow* | light blue* | yellow | yellow | yellow | yellow | yellow* | light red* |
| 11 | Ear form | animal* | animal* | animal ear | animal ear | animal ear | animal ear | animal* | animal* |
| 12 | Horn present | no | no | no | no | **yes** | no | no | no |
| 13 | Horn color | light yellow* | light blue* | yellow* | yellow* | yellow | yellow* | yellow* | light red* |
| 14 | Horn form | sheep* | sheep* | sheep* | sheep* | **bull horn** | sheep* | sheep* | sheep* |
| 15 | Wings present | no | no | no | no | no | no | no | no |
| 16 | Wing color | latent* | latent* | latent* | latent* | latent* | latent* | latent* | latent* |
| 17 | Wing form | feather* | feather* | feather* | feather* | feather* | feather* | feather* | feather* |
| 18 | Tail present | no | no | yes | yes | yes | no | no | no |
| 19 | Tail color | latent* | latent* | yellow | yellow | yellow | latent* | latent* | latent* |
| 20 | Tail form | beast* | beast* | beast tail | beast tail | beast tail | beast* | beast* | beast* |
| 21 | Back feature | no | no | no | no | no | no | no | no |
| 22 | Back color | latent* | latent* | latent* | latent* | latent* | latent* | latent* | latent* |
| 23 | Back form | fin* | fin* | fin* | fin* | fin* | fin* | fin* | fin* |
| 24 | Limbs present | no | no | yes | yes | yes | yes | no | no |
| 25 | Limb color | latent* | latent* | yellow | yellow | yellow | yellow | latent* | latent* |
| 26 | Limb form | small* | small* | standard small animal | standard small animal | standard big animal | standard small animal | small* | small* |
| 27 | Claws present | no | no | no | no | no | no | no | no |
| 28 | Claw color | latent* | latent* | latent* | latent* | latent* | latent* | latent* | latent* |
| 29 | Claw form | sharp* | sharp* | sharp* | sharp* | sharp* | sharp* | sharp* | sharp* |
| 30 | Glow present | no | no | no | no | no | no | **yes** | no |
| 31 | Glow color | latent* | latent* | latent* | latent* | latent* | latent* | yellow | latent* |
| 32 | Glow form | lure* | lure* | lure* | lure* | lure* | lure* | machine indicator | lure* |

\* = part is absent, so the slot is not expressed. The value shown is the **latent** value kept for breeding (set to the body color / first form, so a "no → yes" mutation still produces a coherent offspring). This differs from today's `index.html`, which fills `0` (always "red"); pick one rule and keep it (see DESIGN-genes.md §5.3).

---

## 4. Evidence per pet (how each value was decided)

| pet | measured from the GLB | derived | judgment call |
|---|---|---|---|
| slime-ring | transmission yes, runtime opacity 0.72 / roughness 0.22, single mesh with no separate part ⇒ all 9 part classes = no; avg texture color `#d2ccbd` | body texture = jelly; body form = sphere (user stated the two slimes count as sphere) | body color: **light yellow** (nearest to both average `#d2ccbd` and dominant `#ddd1bd`). Note: today's code uses **white** for this pet — pick one |
| slime-ball | same as above; avg `#79b3d8` | jelly, sphere | none — body color light blue matches today's code |
| knife-shiba | opaque PBR (no transmission), avg `#c4a269` | body color yellow (tan-brown, nearest in palette) | furry texture, sphere form ("shiba ball"), eyes/ears/tail/limbs present, claws absent. **The knife and the shield in the model cannot be expressed by any current gene slot** — structural gap |
| kangaroo-peek | opaque, avg `#e3af52` | yellow | furry, standard mammal, emoji eyes, animal ears, beast tail, small-animal limbs |
| bull-aloof | opaque, avg `#b28b4d`, dominant `#5b4829` | body color **weak**: the 13-color palette has no brown. Chose yellow by hue family (~37 deg) | furry, standard mammal, bull horns (certain), big-animal limbs, beast tail |
| baby-laugh | opaque, avg `#e9ab55` | yellow (peach) | smooth (skin), standard mammal, emoji eyes, animal ears, small-animal limbs, no tail |
| sunny-sun | translucent 0.90 alpha, roughness 0.18, avg `#f1ad3d` | texture = jelly, form = sphere, glow organ = yes | glow form: neither option fits a sun; used **machine indicator**. Table has no "radiating body" — see gaps |
| mind-sphere | opaque, avg `#cc9b95`, dominant `#fd8a8b` | light red (pink) | smooth, sphere, eyes present; limbs unverified (set to no) |

---

## 5. Runtime parameters that are NOT genes

These live in `SPECIES_LIST` and have no gene slot today (documented so nobody "looks for them in the genome"):

| pet | count | speed | body box |
|---|---|---|---|
| slime-ring | 20 | 0.52 | A |
| slime-ball | 20 | 0.72 | A |
| knife-shiba | 10 | 0.95 | **S** |

Offspring speed is currently the average of the two parents' species speed (no movement gene exists in the table).

---

## 6. Open items

1. **Body size box S** (knife-shiba) is not one of the 6 gene grades. Either add S to the table or normalize the shiba to A.
2. **slime-ring color**: code says white, measurement says light yellow — needs your pick.
3. **Accessories** (shiba's knife + shield) have no gene slot; if offspring should be able to carry gear, the table needs a slot (same structural gap DESIGN-genes.md §3.4 describes for models).
4. **Glow form** has no good slot value for a sun-like body.
5. **No GLB yet, concept images only**: `Character_Fusion_BabyBull_GradualChimera_A.png`, `Character_Fusion_BabyBull_UnifiedMascot_B.png`, `Character_Fusion_BabyLaugh_Bull_P1_Concept.png` (baby-laugh x bull hybrids). ~50 credit each once you want them modeled.
6. **No GLB at all**: the 5 procedural species in `SPECIES_LIST` (grazer, scuttler, hopper, ray, bird) — all `spawn: false` today.
7. **Duplicates**: `environment/float_ring.glb` and `environment/float_ball.glb` are the same meshes as pets 1 and 2 (Base variant, jelly transmission off).
