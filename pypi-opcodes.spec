#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-opcodes
Version  : 0.3.14
Release  : 36
URL      : https://files.pythonhosted.org/packages/df/2d/4d98a725b5e73ba3d8588fd415cc64120182ebec78e0695ecae7408a2d74/opcodes-0.3.14.tar.gz
Source0  : https://files.pythonhosted.org/packages/df/2d/4d98a725b5e73ba3d8588fd415cc64120182ebec78e0695ecae7408a2d74/opcodes-0.3.14.tar.gz
Summary  : Database of Processor Instructions/Opcodes
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-opcodes-license = %{version}-%{release}
Requires: pypi-opcodes-python = %{version}-%{release}
Requires: pypi-opcodes-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
.. image:: https://img.shields.io/github/license/Maratyszcza/Opcodes.svg
:alt: License
:target: https://github.com/Maratyszcza/Opcodes/blob/master/license.rst

%package license
Summary: license components for the pypi-opcodes package.
Group: Default

%description license
license components for the pypi-opcodes package.


%package python
Summary: python components for the pypi-opcodes package.
Group: Default
Requires: pypi-opcodes-python3 = %{version}-%{release}

%description python
python components for the pypi-opcodes package.


%package python3
Summary: python3 components for the pypi-opcodes package.
Group: Default
Requires: python3-core
Provides: pypi(opcodes)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-opcodes package.


%prep
%setup -q -n opcodes-0.3.14
cd %{_builddir}/opcodes-0.3.14
pushd ..
cp -a opcodes-0.3.14 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672295198
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-opcodes
cp %{_builddir}/opcodes-%{version}/license.rst %{buildroot}/usr/share/package-licenses/pypi-opcodes/75becd65c0fb973ddc34dd97fb419826c1c1183a || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-opcodes/75becd65c0fb973ddc34dd97fb419826c1c1183a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
