import subprocess as sp
import time

while (True):

	ssh_data = sp.check_output("last -F -a | grep 'still logged in'", shell=True).decode('utf-8')

	ssh_datum = ssh_data.split()

	print(ssh_datum)

	ips = []

	html = open("ActiveSSH.html", 'w+')
	html.write("<!DOCTYPE html>\n<html>\n<head>\n<style>\ntable {\n  width:60%;\n}table, th, td {\n  border: 1px solid white;\n  border-collapse: collapse;\n}th, td {\n  padding: 15px;\n  text-align: left;\n}#t01 tr:nth-child(even) {\n  background-color: #eee;\n}\n#t01 tr:nth-child(odd) {\n background-color: #fff;\n}#t01 th {\n  background-color: #02bd89;\n  color: white;\n}\n</style>\n</head>\n<body>\n\n<h2>Real-Time SSH</h2>")

	html.write("<table id='t01'>\n  <tr>\n    <th>IP-Address</th>\n    <th>Status</th>\n    <th>Logged In Time</th>\n    <th>Last Updated</th>")

	for item in ssh_data.split():
		if item.startswith('10.168.'):
			ips.append(item)

	print(ips)

	for ip in ips:	
		html.write("  <tr>\n    <td>{0}</td>\n    <td>Logged In.</td>\n    <td>{1} {2} {3} {4} {5}</td>\n    <td>{6}</td>\n  </tr>".format(ip, ssh_datum[2], ssh_datum[3], ssh_datum[4], ssh_datum[5], ssh_datum[6], time.asctime(time.localtime(time.time()))))

	html.write("</table>\n</body>\n</html>")
	html.close()

	time.sleep(5)
