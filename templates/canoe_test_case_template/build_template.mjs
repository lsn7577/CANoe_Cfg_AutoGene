import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const buildDir = "F:/Canoe_Gene/templates/canoe_test_case_template";
const outputDir = "F:/Canoe_Gene/templates/canoe_test_case_template";
await fs.mkdir(outputDir, { recursive: true });
const mapping = JSON.parse(await fs.readFile(path.join(buildDir, "template_field_mapping.json"), "utf8"));

const workbook = Workbook.create();
const project = workbook.worksheets.add("工程参数配置");
const cases = workbook.worksheets.add("测试用例");

const colors = {
  navy: "#1F4E78",
  blue: "#5B9BD5",
  paleBlue: "#D9EAF7",
  green: "#70AD47",
  paleGreen: "#E2F0D9",
  yellow: "#FFF2CC",
  grey: "#F2F2F2",
  border: "#BFBFBF",
  text: "#1F2933",
  white: "#FFFFFF",
};

function styleTitle(sheet, range, title) {
  const r = sheet.getRange(range);
  r.merge();
  r.values = [[title]];
  r.format = {
    fill: colors.navy,
    font: { bold: true, color: colors.white, size: 15 },
    wrapText: true,
  };
}

function styleSection(sheet, range, title) {
  const r = sheet.getRange(range);
  r.merge();
  r.values = [[title]];
  r.format = {
    fill: colors.blue,
    font: { bold: true, color: colors.white },
    wrapText: true,
  };
}

function styleHeader(range) {
  range.format = {
    fill: colors.navy,
    font: { bold: true, color: colors.white },
    wrapText: true,
    borders: { preset: "all", style: "thin", color: colors.border },
  };
}

function styleBody(range) {
  range.format = {
    wrapText: true,
    borders: { preset: "all", style: "thin", color: colors.border },
  };
}

function setColumnWidths(sheet, widths) {
  for (const [col, width] of Object.entries(widths)) {
    sheet.getRange(`${col}1:${col}220`).format.columnWidthPx = width;
  }
}

function addListValidation(range, values) {
  range.dataValidation = {
    rule: {
      type: "list",
      values,
    },
  };
}

// Sheet 1: project configuration.
project.showGridLines = false;
styleTitle(project, "A1:N1", "CANoe 自动化测试工程参数配置");
project.getRange("A2:N2").merge();
project.getRange("A2").values = [[
  "填写说明：本表用于描述工程级配置、通信通道和文件挂载。后续 agent/Burr 工作流会优先读取这里的 CANoe 版本、通道、DBC/A2L/CDD 路径和默认超时。",
]];
project.getRange("A2:N2").format = { fill: colors.paleBlue, font: { color: colors.text }, wrapText: true };
project.getRange("A2:N2").format.rowHeightPx = 44;

styleSection(project, "A4:D4", "1. 工程基础配置");
const basicRows = [
  ["配置项", "填写值", "是否必填", "填写说明"],
  ["工程名称", "EQ07_AutoTest_Project", "是", "生成的 CANoe 工程/输出目录基础名称"],
  ["项目代号", "EQ07", "是", "用于报告、CAPL 文件名前缀和日志标识"],
  ["目标 CANoe 版本", "v15", "是", "下拉选择；默认 v15"],
  ["工程输出目录", "F:/Canoe_Gene/generated_projects/EQ07", "是", "生成 cfg、can、dbc、报告等文件的位置"],
  ["测试需求文件路径", "", "否", "可填需求文档、需求矩阵或需求导出文件路径"],
  ["默认 DBC 文件路径", "", "否", "通道未单独填写时使用"],
  ["默认 A2L 文件路径", "", "否", "XCP 标定/观测量解析使用"],
  ["默认 CDD 文件路径", "", "否", "诊断服务解析使用"],
  ["默认测试节点名", "Tester", "是", "CAPL test module / simulation node 默认节点"],
  ["默认诊断 Target", "ECU", "否", "与 CDD/诊断配置中的 target qualifier 对应"],
  ["默认超时 ms", 5000, "是", "用例步骤未填写超时时的默认值"],
  ["测试报告格式", "HTML", "否", "HTML / XML / TXT"],
  ["备注", "", "否", "项目约束、环境要求、特殊说明"],
];
project.getRange("A5:D18").values = basicRows;
styleHeader(project.getRange("A5:D5"));
styleBody(project.getRange("A6:D18"));
project.tables.add("A5:D18", true, "ProjectBasicConfig");
addListValidation(project.getRange("B8"), mapping.canoe_versions);
addListValidation(project.getRange("C6:C18"), mapping.yes_no_values);
addListValidation(project.getRange("B17"), mapping.report_formats);

styleSection(project, "A21:N21", "2. 通信通道与文件挂载配置");
const channelHeaders = mapping.project_config.channel_table_headers;
const channelRows = [channelHeaders];
channelRows.push(["CAN1", "是", "CANFD", "CAN 1", 500000, 2000000, 80, 70, "./dbc/EQ07_CAN1.dbc", "./a2l/EQ07.a2l", "./cdd/EQ07.cdd", "Powertrain", "ECU", "示例，可删除"]);
channelRows.push(["CAN2", "否", "CAN", "CAN 2", 500000, "", 80, "", "", "", "", "", "", ""]);
for (let i = channelRows.length; i < 21; i++) {
  channelRows.push(["", "", "", "", "", "", "", "", "", "", "", "", "", ""]);
}
project.getRange("A22:N42").values = channelRows;
styleHeader(project.getRange("A22:N22"));
styleBody(project.getRange("A23:N42"));
project.tables.add("A22:N42", true, "ChannelMountConfig");
addListValidation(project.getRange("B23:B42"), mapping.yes_no_values);
addListValidation(project.getRange("C23:C42"), mapping.bus_types);

styleSection(project, "A45:D45", "3. 全局生成策略");
const strategyRows = [
  ["策略项", "填写值", "是否必填", "填写说明"],
  ["生成 Test Module", "是", "是", "是否生成测试 CAPL `.can` 文件"],
  ["生成 Simulation Node", "按需", "否", "需要 ECU/总线仿真时启用"],
  ["生成 DBC", "按需", "否", "测试用例中存在缺失报文/信号定义时启用"],
  ["生成 Panel 绑定计划", "按需", "否", "需要人工操作面板或 sysvar 绑定时启用"],
  ["启用团队代码规范", "是", "是", "读取 extras/team/CAPL_Internal_Coding_Standards"],
  ["启用证据链校验", "是", "是", "每个 CAPL API 调用必须能回溯到 KB 页面"],
  ["CAPL生成模式", "llm_with_fallback", "是", "deterministic 固定渲染；llm 严格外部 agent；llm_with_fallback 优先外部 agent，失败回退"],
  ["CANoe 实机编译校验", "否", "否", "本机安装 CANoe 且可自动化时启用"],
];
project.getRange("A46:D54").values = strategyRows;
styleHeader(project.getRange("A46:D46"));
styleBody(project.getRange("A47:D54"));
project.tables.add("A46:D54", true, "GenerationStrategy");
addListValidation(project.getRange("B47:B54"), mapping.strategy_values);
addListValidation(project.getRange("C47:C54"), mapping.yes_no_values);

project.freezePanes.freezeRows(5);
setColumnWidths(project, {
  A: 160, B: 220, C: 90, D: 360, E: 110, F: 120, G: 90, H: 100,
  I: 250, J: 230, K: 230, L: 140, M: 140, N: 220,
});
project.getRange("A1:N60").format.font = { name: "Microsoft YaHei" };
project.getRange("A5:N60").format.rowHeightPx = 28;

// Sheet 2: test cases.
cases.showGridLines = false;
styleTitle(cases, "A1:AA1", "CANoe 自动化测试用例模板");
cases.getRange("A2:AA3").merge();
cases.getRange("A2").values = [[
  "填写说明：一行代表一个步骤/条件/结果组合；同一测试用例包含多个步骤时，复用“用例ID”并递增“步骤序号”。操作类型、条件类型、结果类型均使用下拉框，方便后续工作流结构化解析。",
]];
cases.getRange("A2:AA3").format = { fill: colors.paleBlue, font: { color: colors.text }, wrapText: true };
cases.getRange("A2:AA3").format.rowHeightPx = 56;

const testHeaders = mapping.test_case_columns;
const exampleRows = [
  ["TC_001", "REQ_001", "上电唤醒", "IGN_ON 后 ECU 发送状态报文", "P1", "是", "CAN1 在线，DBC 已挂载", 1, "CAN报文发送", "CAN1", "VehicleCtrl", "IgnitionReq=1; Mode=Normal", 100, 1000, "等待固定时间", "timer", "大于等于", "500ms", 1000, "接收CAN报文发送", "ECU_Status", "存在", "收到至少1帧", 1000, "停发 VehicleCtrl", "示例，可删除", ""],
  ["TC_001", "REQ_001", "上电唤醒", "IGN_ON 后 ECU 发送状态报文", "P1", "是", "CAN1 在线，DBC 已挂载", 2, "CAN信号赋值", "CAN1", "VehicleCtrl.IgnitionReq", "1", "", "", "CAN信号变化", "ECU_Status.Ready", "等于", "1", 3000, "CAN信号变化", "ECU_Status.Ready", "等于", "1", 3000, "", "示例，可删除", ""],
  ["TC_002", "REQ_010", "XCP标定", "修改转速阈值并观察状态", "P2", "是", "A2L 已挂载，XCP 已连接", 1, "XCP标定量赋值", "CAN1", "Cal_RpmThreshold", "1500", "", "", "观测量变化", "Meas_EngineSpeed", "大于等于", "1500", 5000, "观测量变化", "Meas_State", "等于", "ThresholdReached", 5000, "恢复 Cal_RpmThreshold", "示例，可删除", ""],
  ["TC_003", "REQ_020", "诊断会话", "进入扩展会话后读取 DID", "P1", "是", "CDD 已挂载，诊断目标 ECU 可达", 1, "诊断服务请求", "CAN1", "DiagnosticSessionControl", "SID=0x10; sub=0x03", "", "", "诊断服务响应", "DiagnosticSessionControl", "等于", "PositiveResponse", 3000, "诊断服务响应", "ReadDataByIdentifier", "包含", "DID=F190", 3000, "", "示例，可删除", ""],
  ["TC_004", "REQ_030", "人工确认", "人工切换开关后确认信号变化", "P3", "半自动", "测试员在面板前待命", 1, "等待手动操作后确认", "", "手动切换 KL15 开关", "确认后继续", "", "", "等待手动操作后确认", "人工确认", "等于", "已完成", 60000, "CAN信号变化", "ECU_Status.KL15", "等于", "1", 3000, "", "示例，可删除", ""],
];
const caseRows = [testHeaders, ...exampleRows];
for (let i = caseRows.length; i < 201; i++) {
  caseRows.push(new Array(testHeaders.length).fill(""));
}
cases.getRange("A5:AA205").values = caseRows;
styleHeader(cases.getRange("A5:AA5"));
styleBody(cases.getRange("A6:AA205"));
cases.tables.add("A5:AA205", true, "TestCaseStepTable");

// Formula-driven row completeness check.
cases.getRange("AA6").formulas = [[
  '=IF(AND(A6="",H6="",I6="",O6="",T6=""),"",IF(OR(A6="",H6="",I6="",O6="",T6=""),"需补必填项","OK"))',
]];
cases.getRange("AA6:AA205").fillDown();

const operationTypes = mapping.operation_types;
const conditionTypes = mapping.condition_types;
const resultTypes = mapping.result_types;
const priorities = mapping.priority_values;
const automationFlags = mapping.automation_flags;
const compareOps = Object.keys(mapping.compare_operator_mapping);

addListValidation(cases.getRange("E6:E205"), priorities);
addListValidation(cases.getRange("F6:F205"), automationFlags);
addListValidation(cases.getRange("I6:I205"), operationTypes);
addListValidation(cases.getRange("O6:O205"), conditionTypes);
addListValidation(cases.getRange("T6:T205"), resultTypes);
addListValidation(cases.getRange("Q6:Q205"), compareOps);
addListValidation(cases.getRange("V6:V205"), compareOps);

cases.freezePanes.freezeRows(5);
setColumnWidths(cases, {
  A: 90, B: 100, C: 130, D: 210, E: 70, F: 90, G: 220,
  H: 80, I: 150, J: 90, K: 190, L: 240, M: 95, N: 95,
  O: 160, P: 190, Q: 100, R: 160, S: 100,
  T: 160, U: 190, V: 100, W: 170, X: 120, Y: 180, Z: 210, AA: 110,
});
cases.getRange("A1:AA210").format.font = { name: "Microsoft YaHei" };
cases.getRange("A5:AA205").format.rowHeightPx = 34;

// Light highlighting for check column.
cases.getRange("AA6:AA205").conditionalFormats.add("containsText", {
  text: "OK",
  format: { fill: colors.paleGreen, font: { color: "#375623", bold: true } },
});
cases.getRange("AA6:AA205").conditionalFormats.add("containsText", {
  text: "需补",
  format: { fill: "#FCE4D6", font: { color: "#9C0006", bold: true } },
});

// Compact verification artifacts.
const projectPreview = await workbook.render({
  sheetName: "工程参数配置",
  range: "A1:N55",
  scale: 1,
  format: "png",
});
await fs.writeFile(path.join(outputDir, "工程参数配置_preview.png"), new Uint8Array(await projectPreview.arrayBuffer()));

const casesPreview = await workbook.render({
  sheetName: "测试用例",
  range: "A1:AA16",
  scale: 1,
  format: "png",
});
await fs.writeFile(path.join(outputDir, "测试用例_preview.png"), new Uint8Array(await casesPreview.arrayBuffer()));

const inspectProject = await workbook.inspect({
  kind: "table",
  range: "工程参数配置!A5:D18",
  include: "values,formulas",
  tableMaxRows: 16,
  tableMaxCols: 6,
  maxChars: 4000,
});
console.log(inspectProject.ndjson);

const inspectCases = await workbook.inspect({
  kind: "table",
  range: "测试用例!A5:AA11",
  include: "values,formulas",
  tableMaxRows: 8,
  tableMaxCols: 28,
  maxChars: 5000,
});
console.log(inspectCases.ndjson);

const errors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 300 },
  summary: "final formula error scan",
  maxChars: 3000,
});
console.log(errors.ndjson);

const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(path.join(outputDir, "CANoe自动化测试用例模板.xlsx"));
console.log(`saved=${path.join(outputDir, "CANoe自动化测试用例模板.xlsx")}`);
