#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-foreach
Version  : 1.4.4
Release  : 23
URL      : https://cran.r-project.org/src/contrib/foreach_1.4.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/foreach_1.4.4.tar.gz
Summary  : Provides Foreach Looping Construct for R
Group    : Development/Tools
License  : Apache-2.0
Requires: R-iterators
Requires: R-randomForest
BuildRequires : R-iterators
BuildRequires : R-randomForest
BuildRequires : clr-R-helpers

%description
idiom that allows for iterating over elements in a collection,
        without the use of an explicit loop counter.  This package in
        particular is intended to be used for its return value, rather
        than for its side effects.  In that sense, it is similar to the
        standard lapply function, but doesn't require the evaluation
        of a function.  Using foreach without side effects also
        facilitates executing the loop in parallel.

%prep
%setup -q -c -n foreach

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513873978

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1513873978
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library foreach
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library foreach
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library foreach|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/foreach/DESCRIPTION
/usr/lib64/R/library/foreach/INDEX
/usr/lib64/R/library/foreach/Meta/Rd.rds
/usr/lib64/R/library/foreach/Meta/demo.rds
/usr/lib64/R/library/foreach/Meta/features.rds
/usr/lib64/R/library/foreach/Meta/hsearch.rds
/usr/lib64/R/library/foreach/Meta/links.rds
/usr/lib64/R/library/foreach/Meta/nsInfo.rds
/usr/lib64/R/library/foreach/Meta/package.rds
/usr/lib64/R/library/foreach/Meta/vignette.rds
/usr/lib64/R/library/foreach/NAMESPACE
/usr/lib64/R/library/foreach/NEWS
/usr/lib64/R/library/foreach/R/foreach
/usr/lib64/R/library/foreach/R/foreach.rdb
/usr/lib64/R/library/foreach/R/foreach.rdx
/usr/lib64/R/library/foreach/demo/sincSEQ.R
/usr/lib64/R/library/foreach/doc/foreach.R
/usr/lib64/R/library/foreach/doc/foreach.Rnw
/usr/lib64/R/library/foreach/doc/foreach.pdf
/usr/lib64/R/library/foreach/doc/index.html
/usr/lib64/R/library/foreach/doc/nested.R
/usr/lib64/R/library/foreach/doc/nested.Rnw
/usr/lib64/R/library/foreach/doc/nested.pdf
/usr/lib64/R/library/foreach/examples/apply.R
/usr/lib64/R/library/foreach/examples/bigmax.R
/usr/lib64/R/library/foreach/examples/bigmean.R
/usr/lib64/R/library/foreach/examples/bigmean2.R
/usr/lib64/R/library/foreach/examples/bootpar.R
/usr/lib64/R/library/foreach/examples/bootpar2.R
/usr/lib64/R/library/foreach/examples/bootseq.R
/usr/lib64/R/library/foreach/examples/colMeans.R
/usr/lib64/R/library/foreach/examples/comprehensions.R
/usr/lib64/R/library/foreach/examples/cross.R
/usr/lib64/R/library/foreach/examples/feapply.R
/usr/lib64/R/library/foreach/examples/for.R
/usr/lib64/R/library/foreach/examples/germandata.txt
/usr/lib64/R/library/foreach/examples/isplit.R
/usr/lib64/R/library/foreach/examples/matmul.R
/usr/lib64/R/library/foreach/examples/matmul2.R
/usr/lib64/R/library/foreach/examples/output.R
/usr/lib64/R/library/foreach/examples/pi.R
/usr/lib64/R/library/foreach/examples/qsort.R
/usr/lib64/R/library/foreach/examples/rf.R
/usr/lib64/R/library/foreach/examples/sinc.R
/usr/lib64/R/library/foreach/examples/sinc2.R
/usr/lib64/R/library/foreach/examples/sqlite.R
/usr/lib64/R/library/foreach/examples/tuneRF.R
/usr/lib64/R/library/foreach/help/AnIndex
/usr/lib64/R/library/foreach/help/aliases.rds
/usr/lib64/R/library/foreach/help/foreach.rdb
/usr/lib64/R/library/foreach/help/foreach.rdx
/usr/lib64/R/library/foreach/help/paths.rds
/usr/lib64/R/library/foreach/html/00Index.html
/usr/lib64/R/library/foreach/html/R.css
/usr/lib64/R/library/foreach/unitTests/combineTest.R
/usr/lib64/R/library/foreach/unitTests/errorTest.R
/usr/lib64/R/library/foreach/unitTests/foreachTest.R
/usr/lib64/R/library/foreach/unitTests/iteratorTest.R
/usr/lib64/R/library/foreach/unitTests/loadFactorTest.R
/usr/lib64/R/library/foreach/unitTests/mergeTest.R
/usr/lib64/R/library/foreach/unitTests/nestedTest.R
/usr/lib64/R/library/foreach/unitTests/packagesTest.R
/usr/lib64/R/library/foreach/unitTests/runTestSuite.sh
/usr/lib64/R/library/foreach/unitTests/stressTest.R
/usr/lib64/R/library/foreach/unitTests/whenTest.R
