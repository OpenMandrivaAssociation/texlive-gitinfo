# revision 23779
# category Package
# catalog-ctan /macros/latex/contrib/gitinfo
# catalog-date 2011-09-01 15:37:23 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-gitinfo
Version:	1.0
Release:	1
Summary:	Access metadata from the git distributed version control system
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gitinfo
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gitinfo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gitinfo.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package makes it possible to incorporate git version
control metadata into documents. For memoir users, the package
provides the means to tailor page headers and footers to use
the metadata.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gitinfo/gitinfo.sty
%{_texmfdistdir}/tex/latex/gitinfo/gitsetinfo.sty
%doc %{_texmfdistdir}/doc/latex/gitinfo/README
%doc %{_texmfdistdir}/doc/latex/gitinfo/gitHeadInfo.gin
%doc %{_texmfdistdir}/doc/latex/gitinfo/gitinfo.pdf
%doc %{_texmfdistdir}/doc/latex/gitinfo/gitinfo.tex
%doc %{_texmfdistdir}/doc/latex/gitinfo/post-xxx-sample.txt
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
