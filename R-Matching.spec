#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 5424026
#
Name     : R-Matching
Version  : 4.10.15
Release  : 64
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/Matching_4.10-15.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/Matching_4.10-15.tar.gz
Summary  : Multivariate and Propensity Score Matching with Balance
Group    : Development/Tools
License  : GPL-3.0
Requires: R-Matching-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
and for finding optimal balance based on a genetic search algorithm. 
             A variety of univariate and multivariate metrics to
             determine if balance has been obtained are also provided. For
             details, see the paper by Jasjeet Sekhon

%package lib
Summary: lib components for the R-Matching package.
Group: Libraries

%description lib
lib components for the R-Matching package.


%prep
%setup -q -n Matching
pushd ..
cp -a Matching buildavx2
popd
pushd ..
cp -a Matching buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1731645120

%install
export SOURCE_DATE_EPOCH=1731645120
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Matching/CITATION
/usr/lib64/R/library/Matching/DESCRIPTION
/usr/lib64/R/library/Matching/INDEX
/usr/lib64/R/library/Matching/Meta/Rd.rds
/usr/lib64/R/library/Matching/Meta/data.rds
/usr/lib64/R/library/Matching/Meta/demo.rds
/usr/lib64/R/library/Matching/Meta/features.rds
/usr/lib64/R/library/Matching/Meta/hsearch.rds
/usr/lib64/R/library/Matching/Meta/links.rds
/usr/lib64/R/library/Matching/Meta/nsInfo.rds
/usr/lib64/R/library/Matching/Meta/package.rds
/usr/lib64/R/library/Matching/NAMESPACE
/usr/lib64/R/library/Matching/R/Matching
/usr/lib64/R/library/Matching/R/Matching.rdb
/usr/lib64/R/library/Matching/R/Matching.rdx
/usr/lib64/R/library/Matching/data/GerberGreenImai.rda
/usr/lib64/R/library/Matching/data/lalonde.rda
/usr/lib64/R/library/Matching/demo/AbadieImbens.R
/usr/lib64/R/library/Matching/demo/DehejiaWahba.R
/usr/lib64/R/library/Matching/demo/GerberGreenImai.R
/usr/lib64/R/library/Matching/extras/ICC
/usr/lib64/R/library/Matching/extras/Makevars.win.gcc3
/usr/lib64/R/library/Matching/extras/Makevars.win.gcc4
/usr/lib64/R/library/Matching/extras/cblas.h
/usr/lib64/R/library/Matching/extras/cblas_dasum.c
/usr/lib64/R/library/Matching/extras/cblas_dgemm.c
/usr/lib64/R/library/Matching/extras/cblas_dscal.c
/usr/lib64/R/library/Matching/extras/cblas_dsymm.c
/usr/lib64/R/library/Matching/extras/cblas_dtrmm.c
/usr/lib64/R/library/Matching/extras/configure.old
/usr/lib64/R/library/Matching/extras/configure.win
/usr/lib64/R/library/Matching/extras/makefile.cblas
/usr/lib64/R/library/Matching/extras/makefile.icc
/usr/lib64/R/library/Matching/extras/makefile.in
/usr/lib64/R/library/Matching/extras/makefile.osx.in
/usr/lib64/R/library/Matching/extras/makefile.sun
/usr/lib64/R/library/Matching/extras/malloc.c
/usr/lib64/R/library/Matching/help/AnIndex
/usr/lib64/R/library/Matching/help/Matching.rdb
/usr/lib64/R/library/Matching/help/Matching.rdx
/usr/lib64/R/library/Matching/help/aliases.rds
/usr/lib64/R/library/Matching/help/paths.rds
/usr/lib64/R/library/Matching/html/00Index.html
/usr/lib64/R/library/Matching/html/R.css
/usr/lib64/R/library/Matching/tests/testthat.R
/usr/lib64/R/library/Matching/tests/testthat/setup.R
/usr/lib64/R/library/Matching/tests/testthat/test-AbadieImbens.R
/usr/lib64/R/library/Matching/tests/testthat/test-DehejiaWehba.R
/usr/lib64/R/library/Matching/tests/testthat/test-GenMatch.R
/usr/lib64/R/library/Matching/tests/testthat/test-MatchBy.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/Matching/libs/Matching.so
/V4/usr/lib64/R/library/Matching/libs/Matching.so
/usr/lib64/R/library/Matching/libs/Matching.so
