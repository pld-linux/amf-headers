Summary:	AMD Advanced Media Framework (AMF) SDK headers
Summary(pl.UTF-8):	Pliki nagłówkowe AMD Advanced Media Framework (AMF) SDK
Name:		amf-headers
Version:	1.5.3
Release:	1
License:	MIT
Group:		Development/Libraries
#Source0Download: https://github.com/GPUOpen-LibrariesAndSDKs/AMF/tags
Source0:	https://github.com/GPUOpen-LibrariesAndSDKs/AMF/archive/v%{version}/AMF-%{version}.tar.gz
# Source0-md5:	914797ffacfda5ac83a5391f96bb7aa6
URL:		https://gpuopen.com/advanced-media-framework/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The AMD Advanced Media Framework (AMF) SDK provides developers with
optimal access to AMD GPUs for multimedia processing. This package
contains the public headers; the runtime library (libamfrt64.so) is
provided by the AMD GPU driver and loaded with dlopen at run time.

%description -l pl.UTF-8
AMD Advanced Media Framework (AMF) SDK zapewnia programistom optymalny
dostęp do GPU AMD do przetwarzania multimediów. Ten pakiet zawiera
publiczne pliki nagłówkowe; biblioteka wykonawcza (libamfrt64.so)
pochodzi ze sterownika GPU AMD i jest ładowana przez dlopen w czasie
działania.

%prep
%setup -q -n AMF-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/AMF
cp -pr amf/public/include/* $RPM_BUILD_ROOT%{_includedir}/AMF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
%{_includedir}/AMF
