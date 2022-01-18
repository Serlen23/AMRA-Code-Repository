
"use strict";

let WaypointList = require('./WaypointList.js');
let OnboardComputerStatus = require('./OnboardComputerStatus.js');
let Trajectory = require('./Trajectory.js');
let ESCStatusItem = require('./ESCStatusItem.js');
let RTCM = require('./RTCM.js');
let WheelOdomStamped = require('./WheelOdomStamped.js');
let ESCTelemetryItem = require('./ESCTelemetryItem.js');
let PositionTarget = require('./PositionTarget.js');
let Tunnel = require('./Tunnel.js');
let DebugValue = require('./DebugValue.js');
let CameraImageCaptured = require('./CameraImageCaptured.js');
let ESCInfo = require('./ESCInfo.js');
let LogEntry = require('./LogEntry.js');
let BatteryStatus = require('./BatteryStatus.js');
let ESCTelemetry = require('./ESCTelemetry.js');
let CommandCode = require('./CommandCode.js');
let LandingTarget = require('./LandingTarget.js');
let Waypoint = require('./Waypoint.js');
let HilSensor = require('./HilSensor.js');
let StatusText = require('./StatusText.js');
let HilStateQuaternion = require('./HilStateQuaternion.js');
let TerrainReport = require('./TerrainReport.js');
let MagnetometerReporter = require('./MagnetometerReporter.js');
let RadioStatus = require('./RadioStatus.js');
let AttitudeTarget = require('./AttitudeTarget.js');
let HilControls = require('./HilControls.js');
let RCOut = require('./RCOut.js');
let NavControllerOutput = require('./NavControllerOutput.js');
let HomePosition = require('./HomePosition.js');
let GPSINPUT = require('./GPSINPUT.js');
let ParamValue = require('./ParamValue.js');
let GPSRAW = require('./GPSRAW.js');
let RTKBaseline = require('./RTKBaseline.js');
let ExtendedState = require('./ExtendedState.js');
let ManualControl = require('./ManualControl.js');
let PlayTuneV2 = require('./PlayTuneV2.js');
let GPSRTK = require('./GPSRTK.js');
let Mavlink = require('./Mavlink.js');
let Vibration = require('./Vibration.js');
let ActuatorControl = require('./ActuatorControl.js');
let HilActuatorControls = require('./HilActuatorControls.js');
let ADSBVehicle = require('./ADSBVehicle.js');
let GlobalPositionTarget = require('./GlobalPositionTarget.js');
let OpticalFlowRad = require('./OpticalFlowRad.js');
let TimesyncStatus = require('./TimesyncStatus.js');
let Param = require('./Param.js');
let CamIMUStamp = require('./CamIMUStamp.js');
let State = require('./State.js');
let CompanionProcessStatus = require('./CompanionProcessStatus.js');
let HilGPS = require('./HilGPS.js');
let VFR_HUD = require('./VFR_HUD.js');
let WaypointReached = require('./WaypointReached.js');
let FileEntry = require('./FileEntry.js');
let ESCStatus = require('./ESCStatus.js');
let RCIn = require('./RCIn.js');
let VehicleInfo = require('./VehicleInfo.js');
let ESCInfoItem = require('./ESCInfoItem.js');
let OverrideRCIn = require('./OverrideRCIn.js');
let LogData = require('./LogData.js');
let Thrust = require('./Thrust.js');
let MountControl = require('./MountControl.js');
let EstimatorStatus = require('./EstimatorStatus.js');
let Altitude = require('./Altitude.js');

module.exports = {
  WaypointList: WaypointList,
  OnboardComputerStatus: OnboardComputerStatus,
  Trajectory: Trajectory,
  ESCStatusItem: ESCStatusItem,
  RTCM: RTCM,
  WheelOdomStamped: WheelOdomStamped,
  ESCTelemetryItem: ESCTelemetryItem,
  PositionTarget: PositionTarget,
  Tunnel: Tunnel,
  DebugValue: DebugValue,
  CameraImageCaptured: CameraImageCaptured,
  ESCInfo: ESCInfo,
  LogEntry: LogEntry,
  BatteryStatus: BatteryStatus,
  ESCTelemetry: ESCTelemetry,
  CommandCode: CommandCode,
  LandingTarget: LandingTarget,
  Waypoint: Waypoint,
  HilSensor: HilSensor,
  StatusText: StatusText,
  HilStateQuaternion: HilStateQuaternion,
  TerrainReport: TerrainReport,
  MagnetometerReporter: MagnetometerReporter,
  RadioStatus: RadioStatus,
  AttitudeTarget: AttitudeTarget,
  HilControls: HilControls,
  RCOut: RCOut,
  NavControllerOutput: NavControllerOutput,
  HomePosition: HomePosition,
  GPSINPUT: GPSINPUT,
  ParamValue: ParamValue,
  GPSRAW: GPSRAW,
  RTKBaseline: RTKBaseline,
  ExtendedState: ExtendedState,
  ManualControl: ManualControl,
  PlayTuneV2: PlayTuneV2,
  GPSRTK: GPSRTK,
  Mavlink: Mavlink,
  Vibration: Vibration,
  ActuatorControl: ActuatorControl,
  HilActuatorControls: HilActuatorControls,
  ADSBVehicle: ADSBVehicle,
  GlobalPositionTarget: GlobalPositionTarget,
  OpticalFlowRad: OpticalFlowRad,
  TimesyncStatus: TimesyncStatus,
  Param: Param,
  CamIMUStamp: CamIMUStamp,
  State: State,
  CompanionProcessStatus: CompanionProcessStatus,
  HilGPS: HilGPS,
  VFR_HUD: VFR_HUD,
  WaypointReached: WaypointReached,
  FileEntry: FileEntry,
  ESCStatus: ESCStatus,
  RCIn: RCIn,
  VehicleInfo: VehicleInfo,
  ESCInfoItem: ESCInfoItem,
  OverrideRCIn: OverrideRCIn,
  LogData: LogData,
  Thrust: Thrust,
  MountControl: MountControl,
  EstimatorStatus: EstimatorStatus,
  Altitude: Altitude,
};
