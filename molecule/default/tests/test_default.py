"""
Runs Default tests
Available Modules: http://testinfra.readthedocs.io/en/latest/modules.html

"""
import os
import testinfra.utils.ansible_runner

TESTINFRA_HOSTS = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_openssl_is_installed(host):
    """
    Tests that openssl is installed
    """
    openssl = host.package("openssl")
    assert openssl.is_installed


def test_cert_directory(host):
    """
    Tests that the certs and private directory exist
    """
    cert = host.file('/etc/pki/tls/certs')
    private = host.file('/etc/pki/tls/private')

    assert cert.exists
    assert cert.is_directory
    assert private.exists
    assert private.is_directory


def test_self_signed_signature(host):
    """
    Tests openssl can generate self signed certificates
    """
    dist_release = host.ansible(
        "setup")["ansible_facts"]["ansible_distribution_release"]
    cert = host.file('/etc/pki/tls/certs/role_test_cert.crt')
    key = host.file('/etc/pki/tls/private/role_test_cert.key')
    subject_cmd = ("openssl x509 -in "
                   "/etc/pki/tls/certs/role_test_cert.crt -noout -subject"
                   )
    subject_output = ("subject= /C=US/ST=State/L=City/O=Org Name"
                      "/OU=Department Name/CN=role_test_cert"
                      "/emailAddress=admin@fqdn"
                      )

    if dist_release == "bionic":
        subject_output = ("subject=C = US, ST = State, L = City, "
                          "O = Org Name, OU = Department Name, "
                          "CN = role_test_cert, emailAddress = admin@fqdn"
                          )

    subject = host.run(subject_cmd)

    assert cert.exists
    assert cert.is_file
    assert key.exists
    assert key.is_file
    assert subject.stdout == subject_output


def test_cert_and_keys(host):
    """
    Tests this role can copy keypairs
    """
    cert = host.file('/etc/pki/tls/certs/mycert.cer')
    key = host.file('/etc/pki/tls/private/mycert.key')

    assert cert.exists
    assert cert.is_file
    assert 'FAKE_CERT_CONTENT_GOES_HERE' in cert.content_string
    assert key.exists
    assert key.is_file
    assert 'MULTI_LINE_CERT_KEY_GOES_HERE' in key.content_string
