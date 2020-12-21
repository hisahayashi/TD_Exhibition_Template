import subprocess
import psutil

dict_pids = {
    p.info['pid']: p.info['name']
    for p in psutil.process_iter(attrs=['pid', 'name'])
}

if 'TouchDesigner.exe' in dict_pids.values():
	# print('Run TouchDesigner.')
	pass
else:
	# print('Stop TouchDesigner.')
	filepath = r'main.toe'
	subprocess.Popen(['start', filepath], shell=True)
	# print('Restarted TouchDesigner.')

