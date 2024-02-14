import json

DESK_LIGHTS = ['light.desk','light.upper_shelf','light.lower_shelf']

WLED_MAX_BRIGHTNESS = 255


def overhead_lights(light_rgbs=None, light_temp=None, brightness_pct=100):
    if light_rgbs:
        light.turn_on(entity_id='light.sengled_bulb_1', brightness_pct=brightness_pct, rgb_color=light_rgbs[0])
        light.turn_on(entity_id='light.sengled_bulb_2', brightness_pct=brightness_pct, rgb_color=light_rgbs[1])
        light.turn_on(entity_id='light.sengled_bulb_3', brightness_pct=brightness_pct, rgb_color=light_rgbs[2])
    elif light_temp:
        light.turn_on(entity_id='light.sengled_bulb_1', brightness_pct=brightness_pct, color_temp=light_temp)
        light.turn_on(entity_id='light.sengled_bulb_2', brightness_pct=brightness_pct, color_temp=light_temp)
        light.turn_on(entity_id='light.sengled_bulb_3', brightness_pct=brightness_pct, color_temp=light_temp)

def desk_lights(light_rgbs=None, light_temp=None, brightness_pct=100):
    if light_rgbs:
        for i in range(len(DESK_LIGHTS)):
            light.turn_on(entity_id=DESK_LIGHTS[i], brightness_pct=brightness_pct, rgb_color=light_rgbs[i])
    elif light_temp:
        for i in range(len(DESK_LIGHTS)):
            light.turn_on(entity_id=DESK_LIGHTS[i], brightness_pct=brightness_pct, color_temp=light_temp)

def shoe_shelf_off():
    mqtt.publish(topic='wled/shoeshelf/api', payload=json.dumps({"on":False}))

def desk_lights_off():
    mqtt.publish(topic='wled/desklights/api', payload=json.dumps({"on":False}))


def shoe_shelf_rgbw(shelf_rbgw_values, brightness_pct=100):
    brightness = (WLED_MAX_BRIGHTNESS * brightness_pct) // 100
    payload = {"on":True, "seg": [{"col": [shelf_rbgw_value], "bri":brightness, "on":True} for shelf_rbgw_value in shelf_rbgw_values]}
    log.info(json.dumps(payload))
    mqtt.publish(topic='wled/shoeshelf/api', payload=json.dumps(payload))

def desk_lights_rgbw(desk_rgbw_values, brightness_pct=100):
    brightness = (WLED_MAX_BRIGHTNESS * brightness_pct) // 100
    payload = {"on":True, "seg": [{"col": [desk_rgbw_value], "bri":brightness, "on":True} for desk_rgbw_value in desk_rgbw_values]}
    log.info(json.dumps(payload))
    mqtt.publish(topic='wled/desklights/api', payload=json.dumps(payload))

def desk_lights_rgbw_single(desk_rgbw,brightness_pct):
    desk_lights_rgbw([desk_rgbw for i in range(3)], brightness_pct)

def shoe_shelf_rgbw_single(shelf_rgbw,brightness_pct=100):
    shoe_shelf_rgbw([shelf_rgbw for i in range(6)], brightness_pct)

def ge_light(color,brightness=50):
    google_assistant_sdk.send_text_command(command=f'set the ge light color to {color}')
    google_assistant_sdk.send_text_command(command=f'set the ge light brightness to {brightness}')




@service
def test_service(action=None, id=None):
    shoe_shelf_rgbw([[0,0,255,0],[0,0,255,0],[0,0,255,0],[0,0,255,0],[0,0,255,0],[0,0,255,0]],50)

@service
@mqtt_trigger('zigbee2mqtt/officepanel/action', 'payload=="1_single"')
def synthboy_1(action=None, id=None):
    log.info("Synthboy 1 Triggered")
    light.turn_on(entity_id='light.office_lamp', brightness_pct=40, rgb_color=[255,116,86])
    light.turn_on(entity_id='light.office_bed_lights', brightness_pct=100, rgb_color=[127,172,255])
    overhead_lights(light_rgbs=[[30,255,30],[255,30,255],[30,30,255]],brightness_pct=100)
    desk_lights_rgbw(desk_rgbw_values=[[255,0,255],[0,255,200],[115,0,255]],brightness_pct=100)
    shoe_shelf_rgbw_single([255,0,255,0],brightness_pct=100)
    light.turn_on(entity_id='light.daft_punk_sign')
    light.turn_on(entity_id='light.cassetta_sign',brightness_pct=10)
    ge_light('ultramarine')


@service
@mqtt_trigger('zigbee2mqtt/officepanel/action', 'payload=="1_hold"')
def office_lights_off(action=None, id=None):
    google_assistant_sdk.send_text_command(command=f'set the ge light brightness to 0')
    light.turn_off(entity_id='light.cassetta_sign')
    light.turn_off(entity_id='light.daft_punk_sign')
    desk_lights_off()
    light.turn_off(entity_id='light.sengled_bulb_1')
    light.turn_off(entity_id='light.sengled_bulb_2')
    light.turn_off(entity_id='light.sengled_bulb_3')
    light.turn_off(entity_id='light.office_lamp')
    light.turn_off(entity_id='light.office_bed_lights')
    shoe_shelf_off()

@service
@mqtt_trigger('zigbee2mqtt/officepanel/action', 'payload=="2_single"')
def normie_lights_1(action=None, id=None):
    light.turn_off(entity_id='light.office_bed_lights')
    light.turn_off(entity_id='light.cassetta_sign')
    light.turn_off(entity_id='light.daft_punk_sign')
    google_assistant_sdk.send_text_command(command=f'set the ge light brightness to 0')
    overhead_lights(light_temp=300,brightness_pct=100)
    desk_lights_rgbw_single(desk_rgbw=[242,110,0,255],brightness_pct=100)
    light.turn_on(entity_id='light.office_lamp', brightness_pct=100, color_temp=300)
    shoe_shelf_rgbw_single([61,29,0,255],brightness_pct=100)

@service
@mqtt_trigger('zigbee2mqtt/officepanel/action', 'payload=="3_single"')
def redlight(action=None, id=None):
    light.turn_on(entity_id='light.office_lamp', brightness_pct=40, rgb_color=[255,0,0])
    light.turn_on(entity_id='light.office_bed_lights', brightness_pct=100, rgb_color=[255,0,0])
    overhead_lights(light_rgbs=[[255,0,0],[255,0,0],[255,0,0]],brightness_pct=100)
    desk_lights_rgbw_single(desk_rgbw=[255,0,0,0],brightness_pct=100)
    light.turn_off(entity_id='light.daft_punk_sign')
    light.turn_off(entity_id='light.cassetta_sign')
    ge_light('dark red')
    shoe_shelf_rgbw_single([255,0,0,0],brightness_pct=100)


@service
@mqtt_trigger('zigbee2mqtt/officepanel/action', 'payload=="4_single"')
def synthboy_2(action=None, id=None):
    light.turn_on(entity_id='light.office_lamp', brightness_pct=100, rgb_color=[30,255,30])
    light.turn_on(entity_id='light.office_bed_lights', brightness_pct=100, rgb_color=[30,255,0])
    overhead_lights(light_rgbs=[[255,130,30],[255,130,30],[255,130,30]],brightness_pct=100)
    desk_lights_rgbw(desk_rgbw_values=[[255,130,30],[30,255,30],[255,0,255]],brightness_pct=100)
    light.turn_on(entity_id='light.daft_punk_sign')
    light.turn_on(entity_id='light.cassetta_sign',brightness_pct=10)
    ge_light('forest green')
    shoe_shelf_rgbw(brightness_pct=100,shelf_rbgw_values=[[255,130,30],[255,0,255],[30,255,30],[30,255,30],[255,0,255],[255,130,30]])


@service
@mqtt_trigger('zigbee2mqtt/officepanel/action', 'payload=="1_double"')
def sunset(action=None, id=None):
    light.turn_on(entity_id='light.office_lamp', brightness_pct=100, rgb_color=[255,168,38])
    light.turn_on(entity_id='light.office_bed_lights', brightness_pct=100, rgb_color=[255,0,0])
    overhead_lights(light_rgbs=[[255,130,30],[255,15,225],[255,0,0]],brightness_pct=100)
    desk_lights_rgbw(desk_rgbw_values=[[255,130,30],[255,15,225],[255,0,0]],brightness_pct=100)
    light.turn_on(entity_id='light.daft_punk_sign')
    light.turn_on(entity_id='light.cassetta_sign',brightness_pct=10)
    ge_light('magenta')
    shoe_shelf_rgbw(brightness_pct=100,shelf_rbgw_values=[[255,0,0],[255,0,255],[255,130,30],[255,130,30],[255,0,255],[255,0,0]])