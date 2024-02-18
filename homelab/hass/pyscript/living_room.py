

@mqtt_trigger('zigbee2mqtt/living_room_scene_switch/action', 'payload=="1_single"')
def kitchen_toggle(action=None, id=None):
    log.info("hello")
    light.toggle(entity_id='light.kitchen_lights')

@mqtt_trigger('zigbee2mqtt/living_room_scene_switch/action', 'payload=="2_single"')
def dining_toggle(action=None, id=None):
    light.toggle(entity_id='light.dining_room_light',brightness_pct=100)

@mqtt_trigger('zigbee2mqtt/living_room_scene_switch/action', 'payload=="2_double"')
def dining_on_dimmed(action=None, id=None):
    light.turn_on(entity_id='light.dining_room_light',brightness_pct=25)

@mqtt_trigger('zigbee2mqtt/living_room_scene_switch/action', 'payload=="3_single"')
def living_toggle(action=None, id=None):
    light.toggle(entity_id='light.living_room_lights',brightness_pct=100)

@mqtt_trigger('zigbee2mqtt/living_room_scene_switch/action', 'payload=="3_double"')
def living_dimmed(action=None, id=None):
    light.turn_on(entity_id='light.living_room_lights',brightness_pct=25)

@mqtt_trigger('zigbee2mqtt/living_room_scene_switch/action', 'payload=="4_single"')
def living_fan_light_toggle(action=None, id=None):
    light.toggle(entity_id='light.ceiling_fan1')

@mqtt_trigger('zigbee2mqtt/living_room_scene_switch/action', 'payload=="4_double"')
def living_fan_speed_up(action=None, id=None):
    fan.increase_speed(entity_id='fan.ceiling_fan1')

@mqtt_trigger('zigbee2mqtt/living_room_scene_switch/action', 'payload=="1_double"')
def living_fan_speed_down(action=None, id=None):
    fan.decrease_speed(entity_id='fan.ceiling_fan1')

@mqtt_trigger('zigbee2mqtt/living_room_scene_switch/action', 'payload=="4_hold"')
def living_fan_off(action=None, id=None):
    fan.turn_off(entity_id='fan.ceiling_fan1')

@mqtt_trigger('zigbee2mqtt/living_room_scene_switch/action', 'payload=="2_hold"')
def living_fan_reverse(action=None, id=None):
    fan.set_direction(entity_id='fan.ceiling_fan1',direction='forward')


# For ceiling fan on/off methods, it is inconsistent to use in agroup action as the same
# Command is used for both on and off. We would have to rely on state which is flakey
# Until remotes are removed, as toggling with the remote will not result in the state being updated.
@mqtt_trigger('zigbee2mqtt/living_room_scene_switch/action', 'payload=="3_hold"')
def living_kitchen_all_light_off(action=None, id=None):
    # light.turn_off(entity_id='light.ceiling_fan1')
    light.turn_off(entity_id='light.kitchen_lights')
    light.turn_off(entity_id='light.dining_room_light')
    light.turn_off(entity_id='light.living_room_lights')
    # light.turn_off(entity_id='light.ceiling_fan2')

@mqtt_trigger('zigbee2mqtt/living_room_scene_switch/action', 'payload=="1_hold"')
def living_kitchen_all_light_on(action=None, id=None):
    # light.turn_off(entity_id='light.ceiling_fan1')
    light.turn_on(entity_id='light.kitchen_lights')
    light.turn_on(entity_id='light.dining_room_light',brightness_pct=100)
    light.turn_on(entity_id='light.living_room_lights',brightness_pct=100)