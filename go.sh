DEBUG=1
REGISTRY=ghcr.io
OWNER=access-ci-org
REPO=software_modules


function is_windows {
  rv=1
  [[ -n "$USERPROFILE" ]] && rv=0
  return $rv
}


[[ "$DEBUG" -eq 1 ]] && set -x

tag=production
[[ -n "$1" ]] && tag="$1"

action=''
src_home="$HOME"
if is_windows ; then
  action=winpty
  src_home="$USERPROFILE"
fi

$action docker run -it --pull always \
--mount type=bind,src="${src_home}",dst=/home \
--cap-add SYS_ADMIN \
--cap-add DAC_READ_SEARCH \
$REGISTRY/$OWNER/$REPO:$tag
