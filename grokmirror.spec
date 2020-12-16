# TODO: systemd support? (see contrib dir)
Summary:	Framework to smartly mirror git repositories
Summary(pl.UTF-8):	Szkielet do eleganckiego tworzenia kopii lustrzanych repozytoriów git
Name:		grokmirror
Version:	2.0.5
Release:	1
License:	GPL v3+
Group:		Networking/Utilities
Source0:	https://www.kernel.org/pub/software/network/grokmirror/%{name}-%{version}.tar.xz
# Source0-md5:	ea465f9cc8ba77708eae07b5a5b3bfaa
URL:		https://git.kernel.org/cgit/utils/grokmirror/grokmirror.git
BuildRequires:	python3 >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	git-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grokmirror was written to make mirroring large git repository
collections more efficient. Grokmirror uses the manifest file
published by the master mirror in order to figure out which
repositories to clone, and to track which repositories require
updating. The process is extremely lightweight and efficient both for
the master and for the mirrors.

%description -l pl.UTF-8
Grokmirror został napisany, aby poprawić wydajność tworzenia kopii
lustrzanych dużych zbiorów repozytoriów git. Grokmirror używa plik
manifest, opublikowany przez główny serwer, w celu określenia
repozytoriów do klonowania oraz śledzenia, które wymagają
uaktualnienia. Proces jest bardzo lekki i wydajny, zarówno dla serwera
głównego, jak i kopii.

%prep
%setup -q

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst README.rst UPGRADING.rst grokmirror.conf pi-piper.conf
%attr(755,root,root) %{_bindir}/grok-bundle
%attr(755,root,root) %{_bindir}/grok-dumb-pull
%attr(755,root,root) %{_bindir}/grok-fsck
%attr(755,root,root) %{_bindir}/grok-manifest
%attr(755,root,root) %{_bindir}/grok-pi-piper
%attr(755,root,root) %{_bindir}/grok-pull
%{_mandir}/man1/grok-bundle.1*
%{_mandir}/man1/grok-dumb-pull.1*
%{_mandir}/man1/grok-fsck.1*
%{_mandir}/man1/grok-manifest.1*
%{_mandir}/man1/grok-pi-piper.1*
%{_mandir}/man1/grok-pull.1*
%{py3_sitescriptdir}/grokmirror
%{py3_sitescriptdir}/grokmirror-%{version}-py*.egg-info
