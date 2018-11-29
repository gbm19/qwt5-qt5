# https://github.com/gbm19/qwt5-qt5/commit/d07100202ab7d67560ba2c540b49a4972bb1b682
%global commit0 d07100202ab7d67560ba2c540b49a4972bb1b682
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commitdate 20180916

Name:    qwt5-qt5
Version: 5.2.3a
Release: 1.%{commitdate}git%{shortcommit0}%{?dist}
Summary: Qt Widgets for Technical Applications adapted to Qt5

License: LGPLv2 with exceptions
URL:     https://github.com/gbm19/qwt5-qt5

# To get the source code's archive:
# $ curl -OL https://github.com/gbm19/qwt5-qt5/archive/%%{commit0}.zip
#   unzip %%{commit0}.zip
#   mv qwt5-qt5-%%{commit0} qwt5-qt5
#   tar -czvf  qwt5-qt5-%%{commitdate}git%%{shortcommit0}.tar.gz qwt5-qt5
# Alternative method to get the source code
# $ git clone https://github.com/gbm19/qwt5-qt5.git
#   tar -czvf  qwt5-qt5-%%{commitdate}git%%{shortcommit0}.tar.gz qwt5-qt5
Source:  qwt5-qt5-%%{commitdate}git%%{shortcommit0}.tar.gz

BuildRequires: pkgconfig(Qt5Gui) pkgconfig(Qt5Widgets) pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5Svg) pkgconfig(Qt5Designer)

%description
The Qwt library contains GUI Components and utility classes which are primarily
useful for programs with a technical background.
Besides a 2D plot widget it provides scales, sliders, dials, compasses,
thermometers, wheels and knobs to control or display values, arrays
or ranges of type double.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains qt5 libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Extra Developer documentation for %{name}
BuildArch: noarch

%description doc
%{summary}.

%prep
%setup -qc -n qwt5-qt5

pushd qwt5-qt5
# avoid conflicts with qwt5-qt4 man files
for f in doc/man/man3/*.3; do mv $f ${f/%.3/.qt5.3}; done

%build
pushd qwt5-qt5
%{qmake_qt5}
make %{?_smp_mflags}


%install
pushd qwt5-qt5
make install INSTALL_ROOT=%{buildroot}

%ldconfig_scriptlets

%files
%license qwt5-qt5/COPYING
%doc qwt5-qt5/CHANGES
%doc qwt5-qt5/README
%{_qt5_libdir}/lib%{name}.so.*
%{?_qt5_plugindir}/designer/libqwt5_designer_plugin.so

%files devel
%{_mandir}/man3/*
%{_qt5_headerdir}/%{name}/
%{_qt5_libdir}/lib%{name}.so
%{_qt5_libdir}/pkgconfig/%{name}.pc

%files doc
%dir %{_qt5_docdir}
%dir %{_qt5_docdir}/html/
%{_qt5_docdir}/html/%{name}/

%changelog
* Sat Sep 15 2018 Miquel Garriga https://github.com/gbm19 - 5.2.3a-1.20180916gitd071002
- First version using Qt5
