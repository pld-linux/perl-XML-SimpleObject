%include	/usr/lib/rpm/macros.perl
Summary:	XML::SimpleObject perl module
Summary(pl):	Modu³ perla XML::SimpleObject
Name:		perl-XML-SimpleObject
Version:	0.51
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/XML-SimpleObject%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl-XML-LibXML >= 1.30
BuildRequires:	perl-XML-Parser
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::SimpleObject is a small and simple package that takes the output
of XML::Parser as a tree, and gives simple methods for accessing the
structure of an XML document. It is very lightweight, but provides the
simplest access to an XML document possible. It does not subclass
XML::Parser; rather, it is meant to serve purely as an object struct
for an outgoing tree.

%description -l pl
XML::SimpleObject jest ma³ym i prostym pakietem, który przyjmuje
wyj¶cie z XML::Parser jako drzewo i pozwala na ³atwy dostêp do
struktury dokumentu XML. Jest bardzo lekki, ale daje najprostszy
mo¿liwy dostêp do dokumentów XML. Nie jest to podklasa XML::Parser -
natomiast ma s³u¿yæ za obiektow± strukturê dla wychodz±cego drzewa.

%prep
%setup -q -n XML-SimpleObject%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/XML/SimpleObject.pm
%{perl_vendorlib}/XML/SimpleObject
%{perl_vendorlib}/XML/ex.pl
%{_mandir}/man3/*
