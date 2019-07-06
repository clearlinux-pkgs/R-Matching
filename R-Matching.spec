#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Matching
Version  : 4.9.6
Release  : 26
URL      : https://cran.r-project.org/src/contrib/Matching_4.9-6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Matching_4.9-6.tar.gz
Summary  : Multivariate and Propensity Score Matching with Balance
Group    : Development/Tools
License  : GPL-3.0
Requires: R-Matching-lib = %{version}-%{release}
Requires: R-rgenoud
BuildRequires : R-rgenoud
BuildRequires : buildreq-R

%description
## Matching: Multivariate and Propensity Score Matching Software for Causal Inference

%package lib
Summary: lib components for the R-Matching package.
Group: Libraries

%description lib
lib components for the R-Matching package.


%prep
%setup -q -c -n Matching

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557285127

%install
export SOURCE_DATE_EPOCH=1557285127
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Matching
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Matching
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Matching
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc Matching || :


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
/usr/lib64/R/library/Matching/tests/AbadieImbens.R
/usr/lib64/R/library/Matching/tests/AbadieImbens.Rout.save
/usr/lib64/R/library/Matching/tests/DehejiaWahba.R
/usr/lib64/R/library/Matching/tests/DehejiaWahba.Rout.save
/usr/lib64/R/library/Matching/tests/GenMatch.R
/usr/lib64/R/library/Matching/tests/GenMatch.Rout.save
/usr/lib64/R/library/Matching/tests/Matchby.R
/usr/lib64/R/library/Matching/tests/Matchby.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/Matching/libs/Matching.so
/usr/lib64/R/library/Matching/libs/Matching.so.avx2
/usr/lib64/R/library/Matching/libs/Matching.so.avx512
