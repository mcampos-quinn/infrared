set -e

function usage() {
    echo
    echo "    Usage: $0 install_dir prod|dev <optional-tag>"
    echo
    echo "    e.g.   $0 202204220955.cinefiles prod 2.0.3-rc2"
    echo
    exit
}

if [ $# -eq 2 ]; then
    TAG=""
elif [ $# -eq 3 ]; then
    TAG="--branch=$3"
else
    usage
fi

if ! grep -q " $2 " <<< " prod dev "; then
    usage
fi

cd ~/projects
RUN_DIR=$1
if [ -d ${RUN_DIR} ] ; then echo "$1 already exists... exiting" ; exit 1 ; fi

git -c advice.detachedHead=false clone ${TAG} https://github.com/cspace-deployment/radiance.git ${RUN_DIR}
cd ${RUN_DIR}/portal/
gem install bundler -v "$(grep -A 1 "BUNDLED WITH" Gemfile.lock | tail -n 1)"
bundle config set deployment 'false'
bundle update

# migrations and secrets are applied by relink.sh, or you can do them by hand
echo "deployed tag ${TAG} to ${RUN_DIR}, environment is $2"
echo "for deployment on RTL servers, execute:"
echo "./install_ucb.sh <museum>"
echo "./relink.sh ${RUN_DIR} <museum> $2"
echo "then restart Apache, or (re)start some other server."
