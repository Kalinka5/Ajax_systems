import subprocess
import logging


logger = logging.getLogger(__name__)


def get_connected_devices_udids():
    """Function returns all connected devices (their udids)"""

    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
    output_lines = result.stdout.strip().split('\n')

    udids = []
    for line in output_lines[1:]:
        device_id, _ = line.strip().split()
        udids.append(device_id)

    return udids


logger.info("Connected devices UDIDs: %s", get_connected_devices_udids())
