# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       mobile-broadband-provider-info
Summary:    Mobile Broadband Dataprovider Database
Version:    20110511
Release:    1
Group:      Applications/Internet
License:    Creative Commons Public Domain
URL:        http://live.gnome.org/NetworkManager/MobileBroadband/ServiceProviders
Source0:    http://ftp.gnome.org/pub/GNOME/sources/mobile-broadband-provider-info/%{version}/%{name}-%{version}.tar.bz2
Source100:  mobile-broadband-provider-info.yaml
Source101:  mobile-broadband-provider-info-rpmlintrc


%description
This package contains mobile broadband settings for different service providers
in different countries. The Package contains only informational files so it's
safe for distributions to grab updates even during feature freeze and
maintenance stages.

When you want to configure a mobile broadband connections there usually is some
service provider specific information you have to know before the connection
can be established. Problem with this information is that it's highly technical
for an ordinary consumer and it's available only from service providers web
page or from Microsoft Windows installation media that becomes with tie-in
subscription devices.

The interesting side of this information is that it's the same for every user
of a given service provider. This means that service provider specific 
information can be stored in a database. When this database is available the
information can be fetched there and the ordinary user does not need to bother
about it. 

Service provider specific information is stored in a XML file. XML is not the
most optimized format for a database, but it's easy to read, understand and
edit.

The database is released under Creative Commons Public Domain (CC-PD).



%package devel
Summary:    Development files for mobile-broadband-provider-info package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Contains development files for mobile-broadband-provider-info, e.g., .pc file.



%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post









%files
%defattr(-,root,root,-)
# >> files
%{_datadir}/mobile-broadband-provider-info/*
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%doc ChangeLog COPYING NEWS README
%{_datadir}/pkgconfig/mobile-broadband-provider-info.pc
# << files devel

