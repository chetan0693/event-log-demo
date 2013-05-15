Name:		event-log-demo
Version:	0.2
Release:	1%{?dist}
Summary:	Install ElasticSearch + Kibana and configure them to work with Hortonworks Sandbox

Group:		Development/Tools
License:	GPL
URL:		http://hortonworks.com/sandbox
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	elasticsearch, kibana, flume, curl 

%description
Install ElasticSearch + Kibana 3 as well as few pig scripts which will look into an firewall log.

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/event-log-demo-0.2
mkdir -p %{buildroot}/usr/local/bin
cp -ax . %{buildroot}/usr/local/event-log-demo-0.2
cp -ax start_kibana.sh %{buildroot}/usr/local/bin
cp -ax start_flume.sh %{buildroot}/usr/local/bin
cp -ax clean_event_log_demo.sh %{buildroot}/usr/local/bin
cp -ax load_event_log_demo.sh %{buildroot}/usr/local/bin
cp -ax start_event_log_demo.sh %{buildroot}/usr/local/bin

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/local/event-log-demo-0.2/*
%defattr(755,root,root)
/usr/local/bin/*

%doc

%post 
mv /etc/flume/conf/flume.conf /etc/flume/conf/flume.conf.rpmsave
mv /etc/flume/conf/log4j.properties /etc/flume/conf/log4j.properties.rpmsave
cp -ax /usr/local/event-log-demo-0.2/flume.conf /etc/flume/conf/flume.conf
cp -ax /usr/local/event-log-demo-0.2/flume-log4j.properties /etc/flume/conf/log4j.properties

%changelog
* Wed May 15 2013 Olivier Renault <orenault@hortonworks.com> - 0.2
- Update to FW Log 
* Tue May 07 2013 Olivier Renault <orenault@hortonworks.com> - 0.1
- Initial RPM version
