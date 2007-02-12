# TODO:
# - modify the library to build dynamic-one
Summary:	Templates library written in C
Summary(pl.UTF-8):   Biblioteka szablonów napisana w C
Name:		libtemplate
Version:	1.5
Release:	1
License:	unknown
Group:		Libraries
Source0:	http://www.lazarusid.com/download/libs/%{name}-%{version}.tar.gz
# Source0-md5:	9b01650c4f3e51efe9cbb6a1dddcf30d
Patch0:		%{name}-CC.patch
URL:		http://www.lazarusid.com/libtemplate.shtml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you're tired of recompiling your CGI program every time somebody
wants to change the HTML, you need to check out templates. Libtemplate
is an easy to use C interface that will let you use the same sort of
templates used in Lazarus applications.

This software is free to use on any web site, commercial or otherwise.
A technical support contract, including installation and compiling
assistance, may be purchased.

%description -l pl.UTF-8
Jeżeli rekompilowanie programu CGI za każdym razem kiedy ktoś chce
zmienić kod HTML staje się męczące, pora wybróbować szablony.
Libtemplate to łatwy w użyciu interfejs C pozwalający używać tego
samego rodzaju szablonów, co w aplikacjach Lazarusa.

Ten kod jest darmowy do używania na dowolnych stronach WWW, także
komercyjnych. Można natomiast opłacić wsparcie techniczne, wraz z
pomocą przy instalacji i kompilacji.

%package devel
Summary:	Header files for libtemplate library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libtemplate
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libtemplate library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libtemplate.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -fpic"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

%{__make} install \
	INSTALL_DIR=$RPM_BUILD_ROOT%{_prefix} \
	INCLUDE_DIR=$RPM_BUILD_ROOT%{_includedir} \
	LIB_DIR=$RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG template-engine.pdf
#%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
# XXX: move to -static after creating shared lib
%{_libdir}/lib*.a
%{_includedir}/*.h
