#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	XML
%define		pnam	SimpleObject
Summary:	XML::SimpleObject perl module
Summary(pl.UTF-8):	Moduł perla XML::SimpleObject
Name:		perl-XML-SimpleObject
Version:	0.53
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/XML-SimpleObject-%{version}.tar.gz
# Source0-md5:	7826c2f27c36b90bfe731e0001da1021
URL:		http://search.cpan.org/dist/XML-SimpleObject/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-LibXML >= 1.30
BuildRequires:	perl-XML-Parser
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::SimpleObject is a small and simple package that takes the output
of XML::Parser as a tree, and gives simple methods for accessing the
structure of an XML document. It is very lightweight, but provides the
simplest access to an XML document possible. It does not subclass
XML::Parser; rather, it is meant to serve purely as an object struct
for an outgoing tree.

%description -l pl.UTF-8
XML::SimpleObject jest małym i prostym pakietem, który przyjmuje
wyjście z XML::Parser jako drzewo i pozwala na łatwy dostęp do
struktury dokumentu XML. Jest bardzo lekki, ale daje najprostszy
możliwy dostęp do dokumentów XML. Nie jest to podklasa XML::Parser -
natomiast ma służyć za obiektową strukturę dla wychodzącego drzewa.

%prep
%setup -q -n XML-SimpleObject%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/XML/SimpleObject.pm
%{perl_vendorlib}/XML/SimpleObject
%{perl_vendorlib}/XML/ex.pl
%{_mandir}/man3/*
