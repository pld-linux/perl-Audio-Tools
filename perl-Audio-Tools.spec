#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
# 

%ifnarch %{ix86} alpha
%undefine	with_tests
%endif

%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	Tools
Summary:	Audio::Tools Perl module - common tools for some Audio:: modules
Summary(pl.UTF-8):	Moduł Perla Audio::Tools - wspólny kod dla części modułów Audio::
Name:		perl-Audio-Tools
Version:	0.01
Release:	6
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d608a733f373f7bd28d08c0ec6e67116
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The modules in this package are Audio::ByteOrder, Audio::Time and
Audio::Fades. ByteOrder is currently the unpacking rules for little
endian machines, I've seperated this from the other modules for ease
of porting to big endian machines. Fades is a collection of algorithms
for fading in/ out audio files. Time is a collection of tools for
conversion between time, samples & bytes among other things.

%description -l pl.UTF-8
W tym pakiecie znajdują się moduły Audio::ByteOrder, Audio::Time oraz
Audio::Fades. ByteOrder zawiera reguły rozpakowywania dla maszyn
little-endian i jest wydzielony w celu ułatwienia portowania na
maszyny big-endian. Fades to zestaw algorytmów do wyciszania i
nagłaśniania plików dźwiękowych. Time to zestaw narzędzi do konwersji
pomiędzy czasem, próbkami i bajtami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorarch}/Audio/Tools

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Audio/*.pm
%{perl_vendorlib}/Audio/Tools
%{_mandir}/man3/*
