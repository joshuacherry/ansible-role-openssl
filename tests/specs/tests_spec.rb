# encoding: utf-8

control '01' do
  impact 1.0
  title 'Verify openssl'
  desc 'Ensures openssl package'
  
  describe package('openssl') do
    it { should be_installed }
  end

  describe file('/etc/pki/tls/certs') do
    its('type') { should eq :directory }
    it { should be_directory }
  end

  describe file('/etc/pki/tls/private') do
    its('type') { should eq :directory }
    it { should be_directory }
  end

end

control '02' do
  impact 0.9
  title 'Verify Self Signed Certificate'
  desc 'Ensures openssl can generate self signed certificates'

  describe file('/etc/pki/tls/certs/role_test_cert.crt') do
    it { should exist }
  end
  describe file('/etc/pki/tls/private/role_test_cert.key') do
    it { should exist }
  end

  describe x509_certificate('/etc/pki/tls/certs/role_test_cert.crt') do
    its('validity_in_days') { should be >= 3649 }
    its('subject.CN') { should eq "role_test_cert" }
    its('key_length') { should be 2048 }
  end

end

control '02' do
  impact 0.9
  title 'Verify Certificates & Keys'
  desc 'Ensures this role can copy keypairs'

  describe file('/etc/pki/tls/certs/mycert.cer') do
    it { should exist }
  end
  describe file('/etc/pki/tls/private/mycert.key') do
    it { should exist }
  end

  describe file('/etc/pki/tls/certs/mycert.cer') do
    its('content') { should match /FAKE_CERT_CONTENT_GOES_HERE/ }
  end
  describe file('/etc/pki/tls/private/mycert.key') do
    its('content') { should match /MULTI_LINE_CERT_KEY_GOES_HERE/ }
  end

end