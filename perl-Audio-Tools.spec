#
# Conditional build:
# _without_tests - do not perform "make test"

%ifnarch %{ix86} alpha
%define		_without_tests	1
%endif

%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	Tools
Summary:	Audio::Tools Perl module - common tools for some Audio:: modules
Summary(pl):	Modu³ Perla Audio::Tools - wspólny kod dla czê¶ci modu³ów Audio::
Name:		perl-Audio-Tools
Version:	0.01
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The modules in this package are Audio::ByteOrder, Audio::Time and
Audio::Fades. ByteOrder is currently the unpacking rules for little
endian machines, I've seperated this from the other modules for ease
of porting to big endian machines. Fades is a collection of algorithms
for fading in/ out audio files. Time is a collection of tools for
conversion between time, samples & bytes among other things.

%description -l pl
W tym pakiecie znajduj± siê modu³y Audio::ByteOrder, Audio::Time oraz
Audio::Fades. ByteOrder zawiera regu³y rozpakowywania dla maszyn
little-endian i jest wydzielony w celu u³atwienia portowania na
maszyny big-endian. Fades to zestaw algorytmów do wyciszania i
nag³a¶niania plików d¼wiêkowych. Time to zestaw narzêdzi do konwersji
pomiêdzy czasem, próbkami i bajtami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_sitearch}/Audio/Tools

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT{%{perl_sitelib},%{perl_sitearch}}/Audio/Tools/ByteOrder.pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Audio/Tools.pm
%{perl_sitelib}/Audio/Tools
# ByteOrder expects a little-endian machine
%ifarch %{ix86} alpha
%dir %{perl_sitearch}/Audio/Tools
%{perl_sitearch}/Audio/Tools/ByteOrder.pm
%{_mandir}/man3/Audio::Tools::B*
%endif
%{_mandir}/man3/Audio::Tools::[FT]*
%{_mandir}/man3/Audio::Tools.*
