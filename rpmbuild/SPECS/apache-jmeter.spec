Name:		apache-jmeter
Version:	2.9
Release:	1%{?dist}
Summary:	JMeter

Group:		Applications/Internet
License:	Apache License, Version 2.0
URL:		http://jmeter.apache.org/
Source0:	%{name}-%{version}.tgz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
The Apache JMeter™ desktop application is open source software, a 100% pure Java application designed to load test functional behavior and measure performance. It was originally designed for testing Web Applications but has since expanded to other test functions.


%prep
%setup -q


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/%{name}-%{version}
cp -ax . %{buildroot}/usr/local/%{name}-%{version}/

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/usr/local/apache-jmeter-2.9/*

%doc

%changelog
* Tue May 07 2013 Olivier Renault <orenault@hortonworks.com> - 2.9-1
- Initial RPM version
