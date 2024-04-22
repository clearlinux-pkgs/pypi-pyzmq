#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v10
# autospec commit: 5905be9
#
Name     : pypi-pyzmq
Version  : 26.0.2
Release  : 125
URL      : https://files.pythonhosted.org/packages/d4/47/16ca47d3341fcaa4ea1f670c5375953994e2549aabb4950ae32764564e52/pyzmq-26.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/d4/47/16ca47d3341fcaa4ea1f670c5375953994e2549aabb4950ae32764564e52/pyzmq-26.0.2.tar.gz
Summary  : Python bindings for 0MQ
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause LGPL-3.0+ LGPL-3.0-or-later
Requires: pypi-pyzmq-license = %{version}-%{release}
Requires: pypi-pyzmq-python = %{version}-%{release}
Requires: pypi-pyzmq-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : cmake
BuildRequires : libzmq-dev
BuildRequires : pypi(cffi)
BuildRequires : pypi(cython)
BuildRequires : pypi(packaging)
BuildRequires : pypi(scikit_build_core)
BuildRequires : pypi-cython
BuildRequires : pypi-scikit_build
BuildRequires : pypi-scikit_build-python3
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the python bindings.


PyZMQ is a lightweight and super-fast messaging library built on top of
the ZeroMQ library (http://www.zeromq.org).

%package license
Summary: license components for the pypi-pyzmq package.
Group: Default

%description license
license components for the pypi-pyzmq package.


%package python
Summary: python components for the pypi-pyzmq package.
Group: Default
Requires: pypi-pyzmq-python3 = %{version}-%{release}

%description python
python components for the pypi-pyzmq package.


%package python3
Summary: python3 components for the pypi-pyzmq package.
Group: Default
Requires: python3-core
Provides: pypi(pyzmq)
Provides: pypi(pyzmq)

%description python3
python3 components for the pypi-pyzmq package.


%prep
%setup -q -n pyzmq-26.0.2
cd %{_builddir}/pyzmq-26.0.2
pushd ..
cp -a pyzmq-26.0.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713797263
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_CXXFLAGS=$CLEAR_INTERMEDIATE_CFLAGS
CLEAR_INTERMEDIATE_FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_FCFLAGS=$CLEAR_INTERMEDIATE_FFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_CXXFLAGS=$CLEAR_INTERMEDIATE_CFLAGS
CLEAR_INTERMEDIATE_FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_FCFLAGS=$CLEAR_INTERMEDIATE_FFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyzmq
cp %{_builddir}/pyzmq-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-pyzmq/1b42a01e1b763d63d56e3345eb55116593940664 || :
cp %{_builddir}/pyzmq-%{version}/packaging/debian/copyright %{buildroot}/usr/share/package-licenses/pypi-pyzmq/869cbcbc0712a71dc964bf3768a182d018ebdd4b || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyzmq/1b42a01e1b763d63d56e3345eb55116593940664
/usr/share/package-licenses/pypi-pyzmq/869cbcbc0712a71dc964bf3768a182d018ebdd4b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
