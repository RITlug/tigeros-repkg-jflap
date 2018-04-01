Name:      tigeros-repkg-jflap
Version:   7.0
Release:   1%{?dist}
Requires:  java-1.8.0-openjdk
Summary:   Experiment with formal languages topics
URL:       http://www.jflap.org/
License:   See license.html
BuildArch: noarch

Source0: http://www.jflap.org/jflaptmp/may15-2011/withoutSource/JFLAP.jar
Source1: https://www2.cs.duke.edu/csed/jflap/jflaptmp/aug28-09/license.html
Source2: jflap
Source3: JFLAP.desktop
Source4: http://jflap.org/jflapLogo2.jpg

%description
JFLAP is software for experimenting with formal languages and
topics including: nondeterministic finite automata, 
nondeterministic pushdown automata, multi-tape Turing machines, 
several types of grammars, parsing, and L-systems.

%prep
# Pull in remote sources
spectool -g *spec

%install
# Install JFLAP.jar to /usr/share/java
mkdir -p %{buildroot}%{_datadir}/java/
install -p -m 755 %{SOURCE0} %{buildroot}%{_datadir}/java/

# Install license
install -p -m 755 %{SOURCE1} %{buildroot}%{_datadir}/java/

# Install the wrapper script
mkdir -p %{buildroot}%{_prefix}/local/bin/
install -p -m 755 %{SOURCE2} %{buildroot}%{_prefix}/local/bin/

# Install the .desktop file
mkdir -p %{buildroot}%{_prefix}/local/share/applications/
install -p -m 755 %{SOURCE3} %{buildroot}%{_prefix}/local/share/applications/

# Install the icon
mkdir -p %{buildroot}%{_prefix}/local/share/icons/
install -p -m 755 %{SOURCE4} %{buildroot}%{_prefix}/local/share/icons/JFLAP.jpg

%files
%{_prefix}/local/bin/jflap
%{_prefix}/local/share/applications/JFLAP.desktop
%{_prefix}/local/share/icons/JFLAP.jpg
%{_prefix}/share/java/JFLAP.jar
%{_prefix}/share/java/license.html

%changelog
* Sun Apr 01 2018 Tim Zabel <tjz8659@rit.edu> - 7.0-1
- Updated Macros
