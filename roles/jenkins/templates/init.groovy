import hudson.security.*
import jenkins.model.*

// Create default admin user

def instance = Jenkins.getInstance()

if (!instance.isUseSecurity()) {
    def hudsonRealm = new HudsonPrivateSecurityRealm(false)
    hudsonRealm.createAccount('{{ jenkins_admin_username }}', '{{ jenkins_admin_password }}')
    instance.setSecurityRealm(hudsonRealm)

    def strategy = new FullControlOnceLoggedInAuthorizationStrategy()
    instance.setAuthorizationStrategy(strategy)
    instance.save()
}