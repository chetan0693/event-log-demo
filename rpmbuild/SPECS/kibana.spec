Name:		kibana
Version:	0.3.0
Release:	1%{?dist}
Summary:	Make sense of a mountains of logs

Group:		Applications/System
License:	Apache License, Version 2.0
URL:		http://three.kibana.org
Source0:        %{name}-%{version}.tgz

Requires:	npm

%description
Kibana 3 is the even easier way to search, analyze and visualize all of your logs and other machine generated data. As we're installing on the sandbox, we've modified the default port to 38000

%prep
%setup -q


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/kibana-0.3.0/
cp -ax . %{buildroot}/usr/local/kibana-0.3.0/


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/local/kibana-0.3.0/*
%doc

%changelog
* Tue May 07 2013 Olivier Renault <orenault@hortonworks.com> - 0.3.0-1
- Initial RPM version
