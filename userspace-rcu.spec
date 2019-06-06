%define major 6
%define libname %mklibname urcu %major
%define develname %mklibname urcu -d

Name:		userspace-rcu
Summary:	Userspace RCU (read-copy-update) library
Version:	0.11.1
Release:	1
License:	LGPLv2.1+
Group:		System/Libraries
URL:		http://lttng.org/urcu
Source0:	http://lttng.org/files/urcu/%{name}-%{version}.tar.bz2
Patch0:		urcu-generic-buildfix-arm-clang.patch

%description
liburcu is a LGPLv2.1 userspace RCU (read-copy-update) library. This data
synchronization library provides read-side access which scales linearly
with the number of cores. It does so by allowing multiples copies of a given
data structure to live at the same time, and by monitoring the data structure
accesses to detect grace periods after which memory reclamation is possible.

%package -n %{libname}
Summary:	Userspace RCU (read-copy-update) library
Group:		System/Libraries

%description -n %{libname}
liburcu is a LGPLv2.1 userspace RCU (read-copy-update) library. This data
synchronization library provides read-side access which scales linearly
with the number of cores. It does so by allowing multiples copies of a given
data structure to live at the same time, and by monitoring the data structure
accesses to detect grace periods after which memory reclamation is possible.

%package -n %{develname}
Summary:	Development files for liburcu
Group:		Development/C
Requires:	%{libname} = %{version}

%description -n %{develname}
Development file for the userspace RCU library (liburcu).

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/liburcu*.so.%{major}*

%files -n %{develname}
%{_includedir}/urcu/
%{_includedir}/urcu*.h
%{_libdir}/liburcu*.so
%{_libdir}/pkgconfig/liburcu*.pc
%doc %{_docdir}/userspace-rcu
