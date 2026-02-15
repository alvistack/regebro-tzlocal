# Copyright 2026 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-tzlocal
Epoch: 100
Version: 5.3.1
Release: 1%{?dist}
BuildArch: noarch
Summary: tzinfo object for the local timezone
License: MIT
URL: https://github.com/regebro/tzlocal/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip

%description
This Python module returns the IANA time zone name for your local time
zone or a tzinfo object with the local timezone information, under Unix
and Windows.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} >= 1500
%package -n python%{python3_version_nodots}-tzlocal
Summary: tzinfo object for the local timezone
Requires: python3
Provides: python3-tzlocal = %{epoch}:%{version}-%{release}
Provides: python3dist(tzlocal) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-tzlocal = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(tzlocal) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-tzlocal = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(tzlocal) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-tzlocal
This Python module returns the IANA time zone name for your local time
zone or a tzinfo object with the local timezone information, under Unix
and Windows.

%files -n python%{python3_version_nodots}-tzlocal
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} >= 1500)
%package -n python3-tzlocal
Summary: tzinfo object for the local timezone
Requires: python3
Provides: python3-tzlocal = %{epoch}:%{version}-%{release}
Provides: python3dist(tzlocal) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-tzlocal = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(tzlocal) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-tzlocal = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(tzlocal) = %{epoch}:%{version}-%{release}

%description -n python3-tzlocal
This Python module returns the IANA time zone name for your local time
zone or a tzinfo object with the local timezone information, under Unix
and Windows.

%files -n python3-tzlocal
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%changelog
