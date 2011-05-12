%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           rhcpdl
Version:        0.1
Release:        1
Summary:        wget-esque utility for downloading files from Red Hat Customer Portal

Group:          Applications/Internet
License:        GPLv3
URL:            http://rhcpdl.googlecode.com
Source0:        http://rhcpdl.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-setuptools
Requires:       python

%description
A simple cli tool that allows you to cleanly and easily download files from the
Red Hat Customer Portal due to the 2011 changes that made it a multi-step process.

%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} --record=INSTALLED_FILES


%clean
rm -rf %{buildroot}


%files -f INSTALLED_FILES
%defattr(755,root,root,-)
%doc README CHANGELOG INSTALL LICENSE


%changelog
* Wed May 11 2011 Greg Swift <gregswift@gmail.com> 0.1-1
- initial rpm build
