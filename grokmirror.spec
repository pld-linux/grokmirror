Summary:	Framework to smartly mirror git repositories
Name:		grokmirror
Version:	0.3.4
Release:	1
License:	GPL v3+
Group:		Networking/Utilities
Source0:	https://www.kernel.org/pub/software/network/grokmirror/%{name}-%{version}.tar.xz
# Source0-md5:	28384b6799b5f3cf40e8a3dd20f5a346
URL:		https://git.kernel.org/cgit/utils/grokmirror/grokmirror.git
BuildRequires:	python-setuptools
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	python-git
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grokmirror was written to make mirroring large git repository
collections more efficient. Grokmirror uses the manifest file
published by the master mirror in order to figure out which
repositories to clone, and to track which repositories require
updating. The process is extremely lightweight and efficient both for
the master and for the mirrors.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p grok-manifest.py  $RPM_BUILD_ROOT%{_bindir}/grok-manifest
install -p grok-pull.py      $RPM_BUILD_ROOT%{_bindir}/grok-pull
install -p grok-fsck.py      $RPM_BUILD_ROOT%{_bindir}/grok-fsck
install -p grok-dumb-pull.py $RPM_BUILD_ROOT%{_bindir}/grok-dumb-pull
cp -p man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst repos.conf fsck.conf
%attr(755,root,root) %{_bindir}/grok-dumb-pull
%attr(755,root,root) %{_bindir}/grok-fsck
%attr(755,root,root) %{_bindir}/grok-manifest
%attr(755,root,root) %{_bindir}/grok-pull
%{_mandir}/man1/grok-dumb-pull.1*
%{_mandir}/man1/grok-fsck.1*
%{_mandir}/man1/grok-manifest.1*
%{_mandir}/man1/grok-pull.1*
%{py_sitescriptdir}/grokmirror-%{version}-py*.egg-info
%dir %{py_sitescriptdir}/grokmirror
%{py_sitescriptdir}/grokmirror/*.py[co]
