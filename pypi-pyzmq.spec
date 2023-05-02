#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-pyzmq
Version  : 25.0.2
Release  : 113
URL      : https://files.pythonhosted.org/packages/bf/7f/24a55c3393d54570f26fa8845e8e42e813bf1b7fb668ed5d3de76b71dbe9/pyzmq-25.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/bf/7f/24a55c3393d54570f26fa8845e8e42e813bf1b7fb668ed5d3de76b71dbe9/pyzmq-25.0.2.tar.gz
Summary  : Python bindings for 0MQ
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause GPL-3.0
Requires: pypi-pyzmq-license = %{version}-%{release}
Requires: pypi-pyzmq-python = %{version}-%{release}
Requires: pypi-pyzmq-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : libzmq-dev
BuildRequires : pypi-cython
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# PyZMQ: Python bindings for ØMQ
This package contains Python bindings for [ZeroMQ](https://zeromq.org).
ØMQ is a lightweight and fast messaging implementation.

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

%description python3
python3 components for the pypi-pyzmq package.


%prep
%setup -q -n pyzmq-25.0.2
cd %{_builddir}/pyzmq-25.0.2
pushd ..
cp -a pyzmq-25.0.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683047376
export GCC_IGNORE_WERROR=1
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
export CXXFLAGS=$CFLAGS
export FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
export FCFLAGS=$FFLAGS
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyzmq
cp %{_builddir}/pyzmq-%{version}/LICENSE.BSD %{buildroot}/usr/share/package-licenses/pypi-pyzmq/1b42a01e1b763d63d56e3345eb55116593940664 || :
cp %{_builddir}/pyzmq-%{version}/bundled/zeromq/COPYING %{buildroot}/usr/share/package-licenses/pypi-pyzmq/99b1a5c7351fd39a26db3b560ce91eec4a3aca3d || :
cp %{_builddir}/pyzmq-%{version}/bundled/zeromq/external/wepoll/license.txt %{buildroot}/usr/share/package-licenses/pypi-pyzmq/0cf031c01628cf0ee33ed398038238a76ebbd1b7 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyzmq/0cf031c01628cf0ee33ed398038238a76ebbd1b7
/usr/share/package-licenses/pypi-pyzmq/1b42a01e1b763d63d56e3345eb55116593940664
/usr/share/package-licenses/pypi-pyzmq/99b1a5c7351fd39a26db3b560ce91eec4a3aca3d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
