/*************************************** 
 * Car_Panel_Lexical_Decision_V17 Test *
 ***************************************/


// store info about the experiment session:
let expName = 'car_panel_lexical_decision_v17';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
  units: 'pix',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(initializationRoutineBegin());
flowScheduler.add(initializationRoutineEachFrame());
flowScheduler.add(initializationRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'stimuli/panels/large_panel.png', 'path': 'stimuli/panels/large_panel.png'},
    {'name': 'stimuli/panels/background_panel.png', 'path': 'stimuli/panels/background_panel.png'},
    {'name': 'stimulus_sheet.xlsx', 'path': 'stimulus_sheet.xlsx'},
    {'name': 'stimuli/panels/small_panel.png', 'path': 'stimuli/panels/small_panel.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.3';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var initializationClock;
var screen_display_imagesClock;
var background_panel;
var panel1;
var panel2;
var panel3;
var panel4;
var panel5;
var panel6;
var lexical_text_2;
var widget1_symbol1;
var widget1_symbol2;
var widget1_symbol3;
var widget1_text1;
var widget1_text2;
var widget1_text3;
var widget1_text4;
var widget2_symbol1;
var widget2_text1;
var widget2_text2;
var widget3_symbol1;
var widget3_text1;
var widget4_symbol1;
var widget4_text1;
var widget4_text2;
var widget5_text1;
var widget5_symbol1;
var keybaord_input_2;
var background_panel_3;
var inter_trial_intervalClock;
var background_panel_2;
var panel1_2;
var panel2_2;
var panel3_2;
var panel4_2;
var panel5_2;
var panel6_2;
var widget1_symbol1_2;
var widget1_symbol2_2;
var widget1_symbol3_2;
var widget1_text1_2;
var widget1_text2_2;
var widget1_text3_2;
var widget1_text4_2;
var widget2_symbol1_2;
var widget2_text1_2;
var widget2_text2_2;
var widget3_symbol1_2;
var widget3_text1_2;
var widget4_symbol1_2;
var widget4_text1_2;
var widget4_text2_2;
var widget5_text1_2;
var widget5_symbol1_2;
var background_panel_4;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "initialization"
  initializationClock = new util.Clock();
  // Initialize components for Routine "screen_display_images"
  screen_display_imagesClock = new util.Clock();
  background_panel = new visual.ImageStim({
    win : psychoJS.window,
    name : 'background_panel', units : undefined, 
    image : 'stimuli/panels/background_panel.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  panel1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'panel1', units : undefined, 
    image : 'stimuli/panels/large_panel.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  panel2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'panel2', units : undefined, 
    image : 'stimuli/panels/small_panel.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  panel3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'panel3', units : undefined, 
    image : 'stimuli/panels/small_panel.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  panel4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'panel4', units : undefined, 
    image : 'stimuli/panels/small_panel.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  panel5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'panel5', units : undefined, 
    image : 'stimuli/panels/small_panel.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  panel6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'panel6', units : undefined, 
    image : 'stimuli/panels/large_panel.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  lexical_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'lexical_text_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -8.0 
  });
  
  widget1_symbol1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'widget1_symbol1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -9.0 
  });
  widget1_symbol2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'widget1_symbol2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -10.0 
  });
  widget1_symbol3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'widget1_symbol3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -11.0 
  });
  widget1_text1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget1_text1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -12.0 
  });
  
  widget1_text2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget1_text2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -13.0 
  });
  
  widget1_text3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget1_text3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -14.0 
  });
  
  widget1_text4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget1_text4',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: header_wrap_width, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -15.0 
  });
  
  widget2_symbol1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'widget2_symbol1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -16.0 
  });
  widget2_text1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget2_text1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: header_wrap_width, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -17.0 
  });
  
  widget2_text2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget2_text2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -18.0 
  });
  
  widget3_symbol1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'widget3_symbol1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -19.0 
  });
  widget3_text1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget3_text1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -20.0 
  });
  
  widget4_symbol1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'widget4_symbol1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -21.0 
  });
  widget4_text1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget4_text1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -20.0 
  });
  
  widget4_text2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget4_text2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -20.0 
  });
  
  widget5_text1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget5_text1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: header_wrap_width, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -24.0 
  });
  
  widget5_symbol1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'widget5_symbol1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -25.0 
  });
  keybaord_input_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  background_panel_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'background_panel_3', units : undefined, 
    image : 'stimuli/panels/background_panel.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -28.0 
  });
  // Initialize components for Routine "inter_trial_interval"
  inter_trial_intervalClock = new util.Clock();
  background_panel_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'background_panel_2', units : undefined, 
    image : 'stimuli/panels/background_panel.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  panel1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'panel1_2', units : undefined, 
    image : 'stimuli/panels/large_panel.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  panel2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'panel2_2', units : undefined, 
    image : 'stimuli/panels/small_panel.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  panel3_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'panel3_2', units : undefined, 
    image : 'stimuli/panels/small_panel.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  panel4_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'panel4_2', units : undefined, 
    image : 'stimuli/panels/small_panel.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  panel5_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'panel5_2', units : undefined, 
    image : 'stimuli/panels/small_panel.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  panel6_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'panel6_2', units : undefined, 
    image : 'stimuli/panels/large_panel.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  widget1_symbol1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'widget1_symbol1_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  widget1_symbol2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'widget1_symbol2_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -9.0 
  });
  widget1_symbol3_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'widget1_symbol3_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -10.0 
  });
  widget1_text1_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget1_text1_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -11.0 
  });
  
  widget1_text2_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget1_text2_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -12.0 
  });
  
  widget1_text3_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget1_text3_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -13.0 
  });
  
  widget1_text4_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget1_text4_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: header_wrap_width, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -14.0 
  });
  
  widget2_symbol1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'widget2_symbol1_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -15.0 
  });
  widget2_text1_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget2_text1_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: header_wrap_width, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -16.0 
  });
  
  widget2_text2_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget2_text2_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -17.0 
  });
  
  widget3_symbol1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'widget3_symbol1_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -18.0 
  });
  widget3_text1_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget3_text1_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -19.0 
  });
  
  widget4_symbol1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'widget4_symbol1_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -20.0 
  });
  widget4_text1_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget4_text1_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -20.0 
  });
  
  widget4_text2_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget4_text2_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -20.0 
  });
  
  widget5_text1_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'widget5_text1_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: header_wrap_width, ori: 1.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -23.0 
  });
  
  widget5_symbol1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'widget5_symbol1_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -24.0 
  });
  background_panel_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'background_panel_4', units : undefined, 
    image : 'stimuli/panels/background_panel.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -26.0 
  });
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var initializationComponents;
function initializationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'initialization' ---
    t = 0;
    initializationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    initializationComponents = [];
    
    initializationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function initializationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'initialization' ---
    // get current time
    t = initializationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    initializationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function initializationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'initialization' ---
    initializationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "initialization" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'stimulus_sheet.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(screen_display_imagesRoutineBegin(snapshot));
      trialsLoopScheduler.add(screen_display_imagesRoutineEachFrame());
      trialsLoopScheduler.add(screen_display_imagesRoutineEnd(snapshot));
      trialsLoopScheduler.add(inter_trial_intervalRoutineBegin(snapshot));
      trialsLoopScheduler.add(inter_trial_intervalRoutineEachFrame());
      trialsLoopScheduler.add(inter_trial_intervalRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var _keybaord_input_2_allKeys;
var screen_display_imagesComponents;
function screen_display_imagesRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'screen_display_images' ---
    t = 0;
    screen_display_imagesClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    background_panel.setPos(panel_layout.panel_position);
    background_panel.setSize([panel_layout.panel_x_size, panel_layout.panel_y_size]);
    panel1.setPos([widget_regions[0]["x"], widget_regions[0]["y"]]);
    panel1.setSize([widget_regions[0]["width"], widget_regions[0]["height"]]);
    panel2.setPos([widget_regions[1]["x"], widget_regions[1]["y"]]);
    panel2.setSize([widget_regions[1]["width"], widget_regions[1]["height"]]);
    panel3.setPos([widget_regions[2]["x"], widget_regions[2]["y"]]);
    panel3.setSize([widget_regions[2]["width"], widget_regions[2]["height"]]);
    panel4.setPos([widget_regions[3]["x"], widget_regions[3]["y"]]);
    panel4.setSize([widget_regions[3]["width"], widget_regions[3]["height"]]);
    panel5.setPos([widget_regions[4]["x"], widget_regions[4]["y"]]);
    panel5.setSize([widget_regions[4]["width"], widget_regions[4]["height"]]);
    panel6.setPos([widget_regions[5]["x"], widget_regions[5]["y"]]);
    panel6.setSize([widget_regions[5]["width"], widget_regions[5]["height"]]);
    lexical_text_2.setPos([widget_regions[target_panel]["x"], widget_regions[target_panel]["y"]]);
    lexical_text_2.setText(text);
    lexical_text_2.setFont(currentFont);
    lexical_text_2.setHeight(letter_size);
    widget1_symbol1.setPos(correctPositionSmall(all_widgets[0]["image_components"]["duration"]["size_pixel"], all_widgets[0]["image_components"]["duration"]["position_pixel"]));
    widget1_symbol1.setSize(all_widgets[0]["image_components"]["duration"]["size_pixel"]);
    widget1_symbol1.setImage(all_widgets[0]["image_components"]["duration"]["file"]);
    widget1_symbol2.setPos(correctPositionSmall(all_widgets[0]["image_components"]["fuel"]["size_pixel"], all_widgets[0]["image_components"]["fuel"]["position_pixel"]));
    widget1_symbol2.setSize(all_widgets[0]["image_components"]["fuel"]["size_pixel"]);
    widget1_symbol2.setImage(all_widgets[0]["image_components"]["fuel"]["file"]);
    widget1_symbol3.setPos(correctPositionSmall(all_widgets[0]["image_components"]["distance"]["size_pixel"], all_widgets[0]["image_components"]["distance"]["position_pixel"]));
    widget1_symbol3.setSize(all_widgets[0]["image_components"]["distance"]["size_pixel"]);
    widget1_symbol3.setImage(all_widgets[0]["image_components"]["distance"]["file"]);
    widget1_text1.setPos(correctTextPosition(widget1_text1, all_widgets[0]["text_components"]["duration"]["position_pixel"]));
    widget1_text1.setText(all_widgets[0]["text_components"]["duration"]["text"]);
    widget1_text1.setFont(textFont);
    widget1_text1.setHeight(text_size);
    widget1_text2.setPos(correctTextPosition(widget1_text2, all_widgets[0]["text_components"]["fuel"]["position_pixel"]));
    widget1_text2.setText(all_widgets[0]["text_components"]["fuel"]["text"]);
    widget1_text2.setFont(textFont);
    widget1_text2.setHeight(text_size);
    widget1_text3.setPos(correctTextPosition(widget1_text3, all_widgets[0]["text_components"]["distance"]["position_pixel"]));
    widget1_text3.setText(all_widgets[0]["text_components"]["distance"]["text"]);
    widget1_text3.setFont(textFont);
    widget1_text3.setHeight(text_size);
    widget1_text4.setPos(correctTextPosition(widget1_text4, all_widgets[0]["text_components"]["trip_header"]["position_pixel"]));
    widget1_text4.setText(all_widgets[0]["text_components"]["trip_header"]["text"]);
    widget1_text4.setFont(textFont);
    widget1_text4.setHeight(header_size);
    widget2_symbol1.setPos(correctPositionSmall(all_widgets[2]["image_components"]["garage"]["size_pixel"], all_widgets[2]["image_components"]["garage"]["position_pixel"]));
    widget2_symbol1.setSize(all_widgets[2]["image_components"]["garage"]["size_pixel"]);
    widget2_symbol1.setImage(all_widgets[2]["image_components"]["garage"]["file"]);
    widget2_text1.setPos(correctTextPosition(widget2_text1, all_widgets[2]["text_components"]["garage_header"]["position_pixel"]));
    widget2_text1.setText(all_widgets[2]["text_components"]["garage_header"]["text"]);
    widget2_text1.setFont(textFont);
    widget2_text1.setHeight(header_size);
    widget2_text2.setPos(correctTextPosition(widget2_text2, all_widgets[2]["text_components"]["garage_door"]["position_pixel"]));
    widget2_text2.setText(all_widgets[2]["text_components"]["garage_door"]["text"]);
    widget2_text2.setFont(textFont);
    widget2_text2.setHeight(text_size);
    widget3_symbol1.setPos(correctPositionSmall(all_widgets[3]["image_components"]["temperature"]["size_pixel"], all_widgets[3]["image_components"]["temperature"]["position_pixel"]));
    widget3_symbol1.setSize(all_widgets[3]["image_components"]["temperature"]["size_pixel"]);
    widget3_symbol1.setImage(all_widgets[3]["image_components"]["temperature"]["file"]);
    widget3_text1.setPos(correctTextPosition(widget3_text1, all_widgets[3]["text_components"]["temperature"]["position_pixel"]));
    widget3_text1.setText(all_widgets[3]["text_components"]["temperature"]["text"]);
    widget3_text1.setFont(textFont);
    widget3_text1.setHeight(temperature_size);
    widget4_symbol1.setPos(correctPositionSmall(all_widgets[4]["image_components"]["battery"]["size_pixel"], all_widgets[4]["image_components"]["battery"]["position_pixel"]));
    widget4_symbol1.setSize(all_widgets[4]["image_components"]["battery"]["size_pixel"]);
    widget4_symbol1.setImage(all_widgets[4]["image_components"]["battery"]["file"]);
    widget4_text1.setPos(correctTextPosition(widget4_text1, all_widgets[4]["text_components"]["battery"]["position_pixel"]));
    widget4_text1.setText(all_widgets[4]["text_components"]["battery"]["text"]);
    widget4_text1.setFont(textFont);
    widget4_text1.setHeight(battery_size);
    widget4_text2.setPos(correctTextPosition(widget4_text1, all_widgets[4]["text_components"]["miles"]["position_pixel"]));
    widget4_text2.setText(all_widgets[4]["text_components"]["miles"]["text"]);
    widget4_text2.setFont(textFont);
    widget4_text2.setHeight(battery_size);
    widget5_text1.setPos(correctTextPosition(widget5_text1, all_widgets[1]["text_components"]["date"]["position_pixel"]));
    widget5_text1.setOri(0.0);
    widget5_text1.setText(all_widgets[1]["text_components"]["date"]["text"]);
    widget5_text1.setFont(textFont);
    widget5_text1.setHeight(day_size);
    widget5_text1.setFlip('None');
    widget5_symbol1.setPos(correctPositionSmall(all_widgets[1]["image_components"]["calendar"]["size_pixel"], all_widgets[1]["image_components"]["calendar"]["position_pixel"]));
    widget5_symbol1.setSize(all_widgets[1]["image_components"]["calendar"]["size_pixel"]);
    widget5_symbol1.setImage(all_widgets[1]["image_components"]["calendar"]["file"]);
    keybaord_input_2.keys = undefined;
    keybaord_input_2.rt = undefined;
    _keybaord_input_2_allKeys = [];
    // Run 'Begin Routine' code from align_text
    clutter_text1.alignText = "left";
    clutter_text2.alignText = "left";
    clutter_text3.alignText = "left";
    
    background_panel_3.setPos(panel_layout.panel_position);
    background_panel_3.setSize(dummy_panel_size);
    // keep track of which components have finished
    screen_display_imagesComponents = [];
    screen_display_imagesComponents.push(background_panel);
    screen_display_imagesComponents.push(panel1);
    screen_display_imagesComponents.push(panel2);
    screen_display_imagesComponents.push(panel3);
    screen_display_imagesComponents.push(panel4);
    screen_display_imagesComponents.push(panel5);
    screen_display_imagesComponents.push(panel6);
    screen_display_imagesComponents.push(lexical_text_2);
    screen_display_imagesComponents.push(widget1_symbol1);
    screen_display_imagesComponents.push(widget1_symbol2);
    screen_display_imagesComponents.push(widget1_symbol3);
    screen_display_imagesComponents.push(widget1_text1);
    screen_display_imagesComponents.push(widget1_text2);
    screen_display_imagesComponents.push(widget1_text3);
    screen_display_imagesComponents.push(widget1_text4);
    screen_display_imagesComponents.push(widget2_symbol1);
    screen_display_imagesComponents.push(widget2_text1);
    screen_display_imagesComponents.push(widget2_text2);
    screen_display_imagesComponents.push(widget3_symbol1);
    screen_display_imagesComponents.push(widget3_text1);
    screen_display_imagesComponents.push(widget4_symbol1);
    screen_display_imagesComponents.push(widget4_text1);
    screen_display_imagesComponents.push(widget4_text2);
    screen_display_imagesComponents.push(widget5_text1);
    screen_display_imagesComponents.push(widget5_symbol1);
    screen_display_imagesComponents.push(keybaord_input_2);
    screen_display_imagesComponents.push(background_panel_3);
    
    screen_display_imagesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function screen_display_imagesRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'screen_display_images' ---
    // get current time
    t = screen_display_imagesClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *background_panel* updates
    if (t >= 0.0 && background_panel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      background_panel.tStart = t;  // (not accounting for frame time here)
      background_panel.frameNStart = frameN;  // exact frame index
      
      background_panel.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (background_panel.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      background_panel.setAutoDraw(false);
    }
    
    // *panel1* updates
    if (t >= 0.0 && panel1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      panel1.tStart = t;  // (not accounting for frame time here)
      panel1.frameNStart = frameN;  // exact frame index
      
      panel1.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (panel1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      panel1.setAutoDraw(false);
    }
    
    // *panel2* updates
    if (t >= 0.0 && panel2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      panel2.tStart = t;  // (not accounting for frame time here)
      panel2.frameNStart = frameN;  // exact frame index
      
      panel2.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (panel2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      panel2.setAutoDraw(false);
    }
    
    // *panel3* updates
    if (t >= 0.0 && panel3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      panel3.tStart = t;  // (not accounting for frame time here)
      panel3.frameNStart = frameN;  // exact frame index
      
      panel3.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (panel3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      panel3.setAutoDraw(false);
    }
    
    // *panel4* updates
    if (t >= 0.0 && panel4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      panel4.tStart = t;  // (not accounting for frame time here)
      panel4.frameNStart = frameN;  // exact frame index
      
      panel4.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (panel4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      panel4.setAutoDraw(false);
    }
    
    // *panel5* updates
    if (t >= 0.0 && panel5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      panel5.tStart = t;  // (not accounting for frame time here)
      panel5.frameNStart = frameN;  // exact frame index
      
      panel5.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (panel5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      panel5.setAutoDraw(false);
    }
    
    // *panel6* updates
    if (t >= 0.0 && panel6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      panel6.tStart = t;  // (not accounting for frame time here)
      panel6.frameNStart = frameN;  // exact frame index
      
      panel6.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (panel6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      panel6.setAutoDraw(false);
    }
    
    // *lexical_text_2* updates
    if (t >= 0.0 && lexical_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      lexical_text_2.tStart = t;  // (not accounting for frame time here)
      lexical_text_2.frameNStart = frameN;  // exact frame index
      
      lexical_text_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (lexical_text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      lexical_text_2.setAutoDraw(false);
    }
    
    // *widget1_symbol1* updates
    if (t >= 0.0 && widget1_symbol1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget1_symbol1.tStart = t;  // (not accounting for frame time here)
      widget1_symbol1.frameNStart = frameN;  // exact frame index
      
      widget1_symbol1.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget1_symbol1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget1_symbol1.setAutoDraw(false);
    }
    
    // *widget1_symbol2* updates
    if (t >= 0.0 && widget1_symbol2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget1_symbol2.tStart = t;  // (not accounting for frame time here)
      widget1_symbol2.frameNStart = frameN;  // exact frame index
      
      widget1_symbol2.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget1_symbol2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget1_symbol2.setAutoDraw(false);
    }
    
    // *widget1_symbol3* updates
    if (t >= 0.0 && widget1_symbol3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget1_symbol3.tStart = t;  // (not accounting for frame time here)
      widget1_symbol3.frameNStart = frameN;  // exact frame index
      
      widget1_symbol3.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget1_symbol3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget1_symbol3.setAutoDraw(false);
    }
    
    // *widget1_text1* updates
    if (t >= 0.0 && widget1_text1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget1_text1.tStart = t;  // (not accounting for frame time here)
      widget1_text1.frameNStart = frameN;  // exact frame index
      
      widget1_text1.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget1_text1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget1_text1.setAutoDraw(false);
    }
    
    // *widget1_text2* updates
    if (t >= 0.0 && widget1_text2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget1_text2.tStart = t;  // (not accounting for frame time here)
      widget1_text2.frameNStart = frameN;  // exact frame index
      
      widget1_text2.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget1_text2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget1_text2.setAutoDraw(false);
    }
    
    // *widget1_text3* updates
    if (t >= 0.0 && widget1_text3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget1_text3.tStart = t;  // (not accounting for frame time here)
      widget1_text3.frameNStart = frameN;  // exact frame index
      
      widget1_text3.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget1_text3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget1_text3.setAutoDraw(false);
    }
    
    // *widget1_text4* updates
    if (t >= 0.0 && widget1_text4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget1_text4.tStart = t;  // (not accounting for frame time here)
      widget1_text4.frameNStart = frameN;  // exact frame index
      
      widget1_text4.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget1_text4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget1_text4.setAutoDraw(false);
    }
    
    // *widget2_symbol1* updates
    if (t >= 0.0 && widget2_symbol1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget2_symbol1.tStart = t;  // (not accounting for frame time here)
      widget2_symbol1.frameNStart = frameN;  // exact frame index
      
      widget2_symbol1.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget2_symbol1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget2_symbol1.setAutoDraw(false);
    }
    
    // *widget2_text1* updates
    if (t >= 0.0 && widget2_text1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget2_text1.tStart = t;  // (not accounting for frame time here)
      widget2_text1.frameNStart = frameN;  // exact frame index
      
      widget2_text1.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget2_text1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget2_text1.setAutoDraw(false);
    }
    
    // *widget2_text2* updates
    if (t >= 0.0 && widget2_text2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget2_text2.tStart = t;  // (not accounting for frame time here)
      widget2_text2.frameNStart = frameN;  // exact frame index
      
      widget2_text2.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget2_text2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget2_text2.setAutoDraw(false);
    }
    
    // *widget3_symbol1* updates
    if (t >= 0.0 && widget3_symbol1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget3_symbol1.tStart = t;  // (not accounting for frame time here)
      widget3_symbol1.frameNStart = frameN;  // exact frame index
      
      widget3_symbol1.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget3_symbol1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget3_symbol1.setAutoDraw(false);
    }
    
    // *widget3_text1* updates
    if (t >= 0.0 && widget3_text1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget3_text1.tStart = t;  // (not accounting for frame time here)
      widget3_text1.frameNStart = frameN;  // exact frame index
      
      widget3_text1.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget3_text1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget3_text1.setAutoDraw(false);
    }
    
    // *widget4_symbol1* updates
    if (t >= 0.0 && widget4_symbol1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget4_symbol1.tStart = t;  // (not accounting for frame time here)
      widget4_symbol1.frameNStart = frameN;  // exact frame index
      
      widget4_symbol1.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget4_symbol1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget4_symbol1.setAutoDraw(false);
    }
    
    // *widget4_text1* updates
    if (t >= 0.0 && widget4_text1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget4_text1.tStart = t;  // (not accounting for frame time here)
      widget4_text1.frameNStart = frameN;  // exact frame index
      
      widget4_text1.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget4_text1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget4_text1.setAutoDraw(false);
    }
    
    // *widget4_text2* updates
    if (t >= 0.0 && widget4_text2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget4_text2.tStart = t;  // (not accounting for frame time here)
      widget4_text2.frameNStart = frameN;  // exact frame index
      
      widget4_text2.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget4_text2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget4_text2.setAutoDraw(false);
    }
    
    // *widget5_text1* updates
    if (t >= 0.0 && widget5_text1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget5_text1.tStart = t;  // (not accounting for frame time here)
      widget5_text1.frameNStart = frameN;  // exact frame index
      
      widget5_text1.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget5_text1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget5_text1.setAutoDraw(false);
    }
    
    // *widget5_symbol1* updates
    if (t >= 0.0 && widget5_symbol1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget5_symbol1.tStart = t;  // (not accounting for frame time here)
      widget5_symbol1.frameNStart = frameN;  // exact frame index
      
      widget5_symbol1.setAutoDraw(true);
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget5_symbol1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget5_symbol1.setAutoDraw(false);
    }
    
    // *keybaord_input_2* updates
    if (t >= 0.0 && keybaord_input_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keybaord_input_2.tStart = t;  // (not accounting for frame time here)
      keybaord_input_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keybaord_input_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keybaord_input_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keybaord_input_2.clearEvents(); });
    }

    frameRemains = 0.0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (keybaord_input_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      keybaord_input_2.status = PsychoJS.Status.FINISHED;
  }

    if (keybaord_input_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = keybaord_input_2.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _keybaord_input_2_allKeys = _keybaord_input_2_allKeys.concat(theseKeys);
      if (_keybaord_input_2_allKeys.length > 0) {
        keybaord_input_2.keys = _keybaord_input_2_allKeys[_keybaord_input_2_allKeys.length - 1].name;  // just the last key pressed
        keybaord_input_2.rt = _keybaord_input_2_allKeys[_keybaord_input_2_allKeys.length - 1].rt;
        // was this correct?
        if (keybaord_input_2.keys == correct_ans) {
            keybaord_input_2.corr = 1;
        } else {
            keybaord_input_2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *background_panel_3* updates
    if (t >= 0 && background_panel_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      background_panel_3.tStart = t;  // (not accounting for frame time here)
      background_panel_3.frameNStart = frameN;  // exact frame index
      
      background_panel_3.setAutoDraw(true);
    }

    frameRemains = 0 + stim_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (background_panel_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      background_panel_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    screen_display_imagesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function screen_display_imagesRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'screen_display_images' ---
    screen_display_imagesComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (keybaord_input_2.keys === undefined) {
      if (['None','none',undefined].includes(correct_ans)) {
         keybaord_input_2.corr = 1;  // correct non-response
      } else {
         keybaord_input_2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(keybaord_input_2.corr, level);
    }
    psychoJS.experiment.addData('keybaord_input_2.keys', keybaord_input_2.keys);
    psychoJS.experiment.addData('keybaord_input_2.corr', keybaord_input_2.corr);
    if (typeof keybaord_input_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keybaord_input_2.rt', keybaord_input_2.rt);
        routineTimer.reset();
        }
    
    keybaord_input_2.stop();
    // the Routine "screen_display_images" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var alignment_var;
var inter_trial_intervalComponents;
function inter_trial_intervalRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'inter_trial_interval' ---
    t = 0;
    inter_trial_intervalClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    background_panel_2.setPos(panel_layout.panel_position);
    background_panel_2.setSize([panel_layout.panel_x_size, panel_layout.panel_y_size]);
    panel1_2.setPos([widget_regions[0]["x"], widget_regions[0]["y"]]);
    panel1_2.setSize([widget_regions[0]["width"], widget_regions[0]["height"]]);
    panel2_2.setPos([widget_regions[1]["x"], widget_regions[1]["y"]]);
    panel2_2.setSize([widget_regions[1]["width"], widget_regions[1]["height"]]);
    panel3_2.setPos([widget_regions[2]["x"], widget_regions[2]["y"]]);
    panel3_2.setSize([widget_regions[2]["width"], widget_regions[2]["height"]]);
    panel4_2.setPos([widget_regions[3]["x"], widget_regions[3]["y"]]);
    panel4_2.setSize([widget_regions[3]["width"], widget_regions[3]["height"]]);
    panel5_2.setPos([widget_regions[4]["x"], widget_regions[4]["y"]]);
    panel5_2.setSize([widget_regions[4]["width"], widget_regions[4]["height"]]);
    panel6_2.setPos([widget_regions[5]["x"], widget_regions[5]["y"]]);
    panel6_2.setSize([widget_regions[5]["width"], widget_regions[5]["height"]]);
    widget1_symbol1_2.setPos(correctPositionSmall(all_widgets[0]["image_components"]["duration"]["size_pixel"], all_widgets[0]["image_components"]["duration"]["position_pixel"]));
    widget1_symbol1_2.setSize(all_widgets[0]["image_components"]["duration"]["size_pixel"]);
    widget1_symbol1_2.setImage(all_widgets[0]["image_components"]["duration"]["file"]);
    widget1_symbol2_2.setPos(correctPositionSmall(all_widgets[0]["image_components"]["fuel"]["size_pixel"], all_widgets[0]["image_components"]["fuel"]["position_pixel"]));
    widget1_symbol2_2.setSize(all_widgets[0]["image_components"]["fuel"]["size_pixel"]);
    widget1_symbol2_2.setImage(all_widgets[0]["image_components"]["fuel"]["file"]);
    widget1_symbol3_2.setPos(correctPositionSmall(all_widgets[0]["image_components"]["distance"]["size_pixel"], all_widgets[0]["image_components"]["distance"]["position_pixel"]));
    widget1_symbol3_2.setSize(all_widgets[0]["image_components"]["distance"]["size_pixel"]);
    widget1_symbol3_2.setImage(all_widgets[0]["image_components"]["distance"]["file"]);
    widget1_text1_2.setPos(correctTextPosition(widget1_text1, all_widgets[0]["text_components"]["duration"]["position_pixel"]));
    widget1_text1_2.setText(all_widgets[0]["text_components"]["duration"]["text"]);
    widget1_text1_2.setFont(textFont);
    widget1_text1_2.setHeight(text_size);
    widget1_text2_2.setPos(correctTextPosition(widget1_text2, all_widgets[0]["text_components"]["fuel"]["position_pixel"]));
    widget1_text2_2.setText(all_widgets[0]["text_components"]["fuel"]["text"]);
    widget1_text2_2.setFont(textFont);
    widget1_text2_2.setHeight(text_size);
    widget1_text3_2.setPos(correctTextPosition(widget1_text3, all_widgets[0]["text_components"]["distance"]["position_pixel"]));
    widget1_text3_2.setText(all_widgets[0]["text_components"]["distance"]["text"]);
    widget1_text3_2.setFont(textFont);
    widget1_text3_2.setHeight(text_size);
    widget1_text4_2.setPos(correctTextPosition(widget1_text4, all_widgets[0]["text_components"]["trip_header"]["position_pixel"]));
    widget1_text4_2.setText(all_widgets[0]["text_components"]["trip_header"]["text"]);
    widget1_text4_2.setFont(textFont);
    widget1_text4_2.setHeight(header_size);
    widget2_symbol1_2.setPos(correctPositionSmall(all_widgets[2]["image_components"]["garage"]["size_pixel"], all_widgets[2]["image_components"]["garage"]["position_pixel"]));
    widget2_symbol1_2.setSize(all_widgets[2]["image_components"]["garage"]["size_pixel"]);
    widget2_symbol1_2.setImage(all_widgets[2]["image_components"]["garage"]["file"]);
    widget2_text1_2.setPos(correctTextPosition(widget2_text1, all_widgets[2]["text_components"]["garage_header"]["position_pixel"]));
    widget2_text1_2.setText(all_widgets[2]["text_components"]["garage_header"]["text"]);
    widget2_text1_2.setFont(textFont);
    widget2_text1_2.setHeight(header_size);
    widget2_text2_2.setPos(correctTextPosition(widget2_text2, all_widgets[2]["text_components"]["garage_door"]["position_pixel"]));
    widget2_text2_2.setText(all_widgets[2]["text_components"]["garage_door"]["text"]);
    widget2_text2_2.setFont(textFont);
    widget2_text2_2.setHeight(text_size);
    widget3_symbol1_2.setPos(correctPositionSmall(all_widgets[3]["image_components"]["temperature"]["size_pixel"], all_widgets[3]["image_components"]["temperature"]["position_pixel"]));
    widget3_symbol1_2.setSize(all_widgets[3]["image_components"]["temperature"]["size_pixel"]);
    widget3_symbol1_2.setImage(all_widgets[3]["image_components"]["temperature"]["file"]);
    widget3_text1_2.setPos(correctTextPosition(widget3_text1, all_widgets[3]["text_components"]["temperature"]["position_pixel"]));
    widget3_text1_2.setText(all_widgets[3]["text_components"]["temperature"]["text"]);
    widget3_text1_2.setFont(textFont);
    widget3_text1_2.setHeight(temperature_size);
    widget4_symbol1_2.setPos(correctPositionSmall(all_widgets[4]["image_components"]["battery"]["size_pixel"], all_widgets[4]["image_components"]["battery"]["position_pixel"]));
    widget4_symbol1_2.setSize(all_widgets[4]["image_components"]["battery"]["size_pixel"]);
    widget4_symbol1_2.setImage(all_widgets[4]["image_components"]["battery"]["file"]);
    widget4_text1_2.setPos(correctTextPosition(widget4_text1, all_widgets[4]["text_components"]["battery"]["position_pixel"]));
    widget4_text1_2.setText(all_widgets[4]["text_components"]["battery"]["text"]);
    widget4_text1_2.setFont(textFont);
    widget4_text1_2.setHeight(battery_size);
    widget4_text2_2.setPos(correctTextPosition(widget4_text1, all_widgets[4]["text_components"]["miles"]["position_pixel"]));
    widget4_text2_2.setText(all_widgets[4]["text_components"]["miles"]["text"]);
    widget4_text2_2.setFont(textFont);
    widget4_text2_2.setHeight(battery_size);
    widget5_text1_2.setPos(correctTextPosition(widget5_text1, all_widgets[1]["text_components"]["date"]["position_pixel"]));
    widget5_text1_2.setOri(0.0);
    widget5_text1_2.setText(all_widgets[1]["text_components"]["date"]["text"]);
    widget5_text1_2.setFont(textFont);
    widget5_text1_2.setHeight(day_size);
    widget5_text1_2.setFlip('None');
    widget5_symbol1_2.setPos(correctPositionSmall(all_widgets[1]["image_components"]["calendar"]["size_pixel"], all_widgets[1]["image_components"]["calendar"]["position_pixel"]));
    widget5_symbol1_2.setSize(all_widgets[1]["image_components"]["calendar"]["size_pixel"]);
    widget5_symbol1_2.setImage(all_widgets[1]["image_components"]["calendar"]["file"]);
    // Run 'Begin Routine' code from align_text_2
    clutter_text1.alignText = "left";
    clutter_text2.alignText = "left";
    clutter_text3.alignText = "left";
    
    background_panel_4.setPos(panel_layout.panel_position);
    background_panel_4.setSize(dummy_panel_size);
    // Run 'Begin Routine' code from text_align
    alignment_var = "left";
    widget1_text4_2.bold = true;
    widget2_text1_2.bold = true;
    widget3_text1_2.bold = true;
    widget4_text1_2.bold = true;
    widget4_text2_2.bold = true;
    widget5_text1_2.bold = true;
    
    // keep track of which components have finished
    inter_trial_intervalComponents = [];
    inter_trial_intervalComponents.push(background_panel_2);
    inter_trial_intervalComponents.push(panel1_2);
    inter_trial_intervalComponents.push(panel2_2);
    inter_trial_intervalComponents.push(panel3_2);
    inter_trial_intervalComponents.push(panel4_2);
    inter_trial_intervalComponents.push(panel5_2);
    inter_trial_intervalComponents.push(panel6_2);
    inter_trial_intervalComponents.push(widget1_symbol1_2);
    inter_trial_intervalComponents.push(widget1_symbol2_2);
    inter_trial_intervalComponents.push(widget1_symbol3_2);
    inter_trial_intervalComponents.push(widget1_text1_2);
    inter_trial_intervalComponents.push(widget1_text2_2);
    inter_trial_intervalComponents.push(widget1_text3_2);
    inter_trial_intervalComponents.push(widget1_text4_2);
    inter_trial_intervalComponents.push(widget2_symbol1_2);
    inter_trial_intervalComponents.push(widget2_text1_2);
    inter_trial_intervalComponents.push(widget2_text2_2);
    inter_trial_intervalComponents.push(widget3_symbol1_2);
    inter_trial_intervalComponents.push(widget3_text1_2);
    inter_trial_intervalComponents.push(widget4_symbol1_2);
    inter_trial_intervalComponents.push(widget4_text1_2);
    inter_trial_intervalComponents.push(widget4_text2_2);
    inter_trial_intervalComponents.push(widget5_text1_2);
    inter_trial_intervalComponents.push(widget5_symbol1_2);
    inter_trial_intervalComponents.push(background_panel_4);
    
    inter_trial_intervalComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function inter_trial_intervalRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'inter_trial_interval' ---
    // get current time
    t = inter_trial_intervalClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *background_panel_2* updates
    if (t >= 0.0 && background_panel_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      background_panel_2.tStart = t;  // (not accounting for frame time here)
      background_panel_2.frameNStart = frameN;  // exact frame index
      
      background_panel_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (background_panel_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      background_panel_2.setAutoDraw(false);
    }
    
    // *panel1_2* updates
    if (t >= 0.0 && panel1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      panel1_2.tStart = t;  // (not accounting for frame time here)
      panel1_2.frameNStart = frameN;  // exact frame index
      
      panel1_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (panel1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      panel1_2.setAutoDraw(false);
    }
    
    // *panel2_2* updates
    if (t >= 0.0 && panel2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      panel2_2.tStart = t;  // (not accounting for frame time here)
      panel2_2.frameNStart = frameN;  // exact frame index
      
      panel2_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (panel2_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      panel2_2.setAutoDraw(false);
    }
    
    // *panel3_2* updates
    if (t >= 0.0 && panel3_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      panel3_2.tStart = t;  // (not accounting for frame time here)
      panel3_2.frameNStart = frameN;  // exact frame index
      
      panel3_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (panel3_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      panel3_2.setAutoDraw(false);
    }
    
    // *panel4_2* updates
    if (t >= 0.0 && panel4_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      panel4_2.tStart = t;  // (not accounting for frame time here)
      panel4_2.frameNStart = frameN;  // exact frame index
      
      panel4_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (panel4_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      panel4_2.setAutoDraw(false);
    }
    
    // *panel5_2* updates
    if (t >= 0.0 && panel5_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      panel5_2.tStart = t;  // (not accounting for frame time here)
      panel5_2.frameNStart = frameN;  // exact frame index
      
      panel5_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (panel5_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      panel5_2.setAutoDraw(false);
    }
    
    // *panel6_2* updates
    if (t >= 0.0 && panel6_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      panel6_2.tStart = t;  // (not accounting for frame time here)
      panel6_2.frameNStart = frameN;  // exact frame index
      
      panel6_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (panel6_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      panel6_2.setAutoDraw(false);
    }
    
    // *widget1_symbol1_2* updates
    if (t >= 0.0 && widget1_symbol1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget1_symbol1_2.tStart = t;  // (not accounting for frame time here)
      widget1_symbol1_2.frameNStart = frameN;  // exact frame index
      
      widget1_symbol1_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget1_symbol1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget1_symbol1_2.setAutoDraw(false);
    }
    
    // *widget1_symbol2_2* updates
    if (t >= 0.0 && widget1_symbol2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget1_symbol2_2.tStart = t;  // (not accounting for frame time here)
      widget1_symbol2_2.frameNStart = frameN;  // exact frame index
      
      widget1_symbol2_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget1_symbol2_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget1_symbol2_2.setAutoDraw(false);
    }
    
    // *widget1_symbol3_2* updates
    if (t >= 0.0 && widget1_symbol3_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget1_symbol3_2.tStart = t;  // (not accounting for frame time here)
      widget1_symbol3_2.frameNStart = frameN;  // exact frame index
      
      widget1_symbol3_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget1_symbol3_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget1_symbol3_2.setAutoDraw(false);
    }
    
    // *widget1_text1_2* updates
    if (t >= 0.0 && widget1_text1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget1_text1_2.tStart = t;  // (not accounting for frame time here)
      widget1_text1_2.frameNStart = frameN;  // exact frame index
      
      widget1_text1_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget1_text1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget1_text1_2.setAutoDraw(false);
    }
    
    // *widget1_text2_2* updates
    if (t >= 0.0 && widget1_text2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget1_text2_2.tStart = t;  // (not accounting for frame time here)
      widget1_text2_2.frameNStart = frameN;  // exact frame index
      
      widget1_text2_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget1_text2_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget1_text2_2.setAutoDraw(false);
    }
    
    // *widget1_text3_2* updates
    if (t >= 0.0 && widget1_text3_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget1_text3_2.tStart = t;  // (not accounting for frame time here)
      widget1_text3_2.frameNStart = frameN;  // exact frame index
      
      widget1_text3_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget1_text3_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget1_text3_2.setAutoDraw(false);
    }
    
    // *widget1_text4_2* updates
    if (t >= 0.0 && widget1_text4_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget1_text4_2.tStart = t;  // (not accounting for frame time here)
      widget1_text4_2.frameNStart = frameN;  // exact frame index
      
      widget1_text4_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget1_text4_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget1_text4_2.setAutoDraw(false);
    }
    
    // *widget2_symbol1_2* updates
    if (t >= 0.0 && widget2_symbol1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget2_symbol1_2.tStart = t;  // (not accounting for frame time here)
      widget2_symbol1_2.frameNStart = frameN;  // exact frame index
      
      widget2_symbol1_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget2_symbol1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget2_symbol1_2.setAutoDraw(false);
    }
    
    // *widget2_text1_2* updates
    if (t >= 0.0 && widget2_text1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget2_text1_2.tStart = t;  // (not accounting for frame time here)
      widget2_text1_2.frameNStart = frameN;  // exact frame index
      
      widget2_text1_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget2_text1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget2_text1_2.setAutoDraw(false);
    }
    
    // *widget2_text2_2* updates
    if (t >= 0.0 && widget2_text2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget2_text2_2.tStart = t;  // (not accounting for frame time here)
      widget2_text2_2.frameNStart = frameN;  // exact frame index
      
      widget2_text2_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget2_text2_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget2_text2_2.setAutoDraw(false);
    }
    
    // *widget3_symbol1_2* updates
    if (t >= 0.0 && widget3_symbol1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget3_symbol1_2.tStart = t;  // (not accounting for frame time here)
      widget3_symbol1_2.frameNStart = frameN;  // exact frame index
      
      widget3_symbol1_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget3_symbol1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget3_symbol1_2.setAutoDraw(false);
    }
    
    // *widget3_text1_2* updates
    if (t >= 0.0 && widget3_text1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget3_text1_2.tStart = t;  // (not accounting for frame time here)
      widget3_text1_2.frameNStart = frameN;  // exact frame index
      
      widget3_text1_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget3_text1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget3_text1_2.setAutoDraw(false);
    }
    
    // *widget4_symbol1_2* updates
    if (t >= 0.0 && widget4_symbol1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget4_symbol1_2.tStart = t;  // (not accounting for frame time here)
      widget4_symbol1_2.frameNStart = frameN;  // exact frame index
      
      widget4_symbol1_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget4_symbol1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget4_symbol1_2.setAutoDraw(false);
    }
    
    // *widget4_text1_2* updates
    if (t >= 0.0 && widget4_text1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget4_text1_2.tStart = t;  // (not accounting for frame time here)
      widget4_text1_2.frameNStart = frameN;  // exact frame index
      
      widget4_text1_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget4_text1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget4_text1_2.setAutoDraw(false);
    }
    
    // *widget4_text2_2* updates
    if (t >= 0.0 && widget4_text2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget4_text2_2.tStart = t;  // (not accounting for frame time here)
      widget4_text2_2.frameNStart = frameN;  // exact frame index
      
      widget4_text2_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget4_text2_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget4_text2_2.setAutoDraw(false);
    }
    
    // *widget5_text1_2* updates
    if (t >= 0.0 && widget5_text1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget5_text1_2.tStart = t;  // (not accounting for frame time here)
      widget5_text1_2.frameNStart = frameN;  // exact frame index
      
      widget5_text1_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget5_text1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget5_text1_2.setAutoDraw(false);
    }
    
    // *widget5_symbol1_2* updates
    if (t >= 0.0 && widget5_symbol1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      widget5_symbol1_2.tStart = t;  // (not accounting for frame time here)
      widget5_symbol1_2.frameNStart = frameN;  // exact frame index
      
      widget5_symbol1_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (widget5_symbol1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      widget5_symbol1_2.setAutoDraw(false);
    }
    
    // *background_panel_4* updates
    if (t >= 0 && background_panel_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      background_panel_4.tStart = t;  // (not accounting for frame time here)
      background_panel_4.frameNStart = frameN;  // exact frame index
      
      background_panel_4.setAutoDraw(true);
    }

    frameRemains = 0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (background_panel_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      background_panel_4.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    inter_trial_intervalComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function inter_trial_intervalRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'inter_trial_interval' ---
    inter_trial_intervalComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "inter_trial_interval" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
