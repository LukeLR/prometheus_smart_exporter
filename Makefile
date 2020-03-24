PREFIX ?= /usr/local

systemd_units = $(wildcard systemd/*.service) $(wildcard systemd/*.socket)

all:

install:
	install -m 644 $(systemd_units) /etc/systemd/system/
	install -m 755 -d /etc/prometheus_smart_exporter/
	install -m 755 devices.json /etc/prometheus_smart_exporter/
	install -m 755 prometheus_smart_exporter/data/attrmap.json /etc/prometheus_smart_exporter/

	systemctl daemon-reload
	systemctl enable prometheus_smart_helper.service
	systemctl enable prometheus_smart_helper.socket
	systemctl enable prometheus_smart_exporter.service

	systemctl start prometheus_smart_helper.socket
	systemctl start prometheus_smart_helper.service
	systemctl start prometheus_smart_exporter.service
.PHONY: install
