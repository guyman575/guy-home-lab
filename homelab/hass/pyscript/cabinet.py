@mqtt_trigger('zigbee2mqtt/pantry_door_sensor_1')
def cabinet(payload_obj):
    log.info("Triggered cabionet routine")
    if 'contact' not in payload_obj:
        log.info("NO CONTACT INFO, RETURN")
        return
    if not payload_obj['contact']:
        log.info("TURN ON FROM NO CONTACT")
        light.turn_on(entity_id='light.pantry_lights')
    else:
        log.info("TURN OFF FROM NO CONTACT")
        light.turn_off(entity_id='light.pantry_lights')