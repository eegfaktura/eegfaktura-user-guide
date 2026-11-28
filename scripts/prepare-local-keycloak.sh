#!/usr/bin/env bash
# Optional companion of prepare-local-stack.sql, ONLY for the local eegfaktura-dev stack: the fixture admin
# rc100100-admin gets a realistic name and e-mail for the user menu screenshot. Run it in the WSL distribution of the
# stack (bash scripts/prepare-local-keycloak.sh); the realm import of the next stack start resets the user.
set -euo pipefail
cd "${EEGF_DEV:-$HOME/eegfaktura-dev}"
pw=$(grep -m1 KC_BOOTSTRAP_ADMIN_PASSWORD docker-compose-local.yml | awk '{print $2}')
docker compose -f docker-compose-local.yml exec -T -e PW="$pw" eegfaktura-keycloak bash -c '
k=/opt/keycloak/bin/kcadm.sh
$k config credentials --config /tmp/kc.cfg --server http://localhost:8080 --realm master --user admin --password "$PW" >/dev/null
id=$($k get users --config /tmp/kc.cfg -r EEGFaktura -q username=rc100100-admin -q exact=true --fields id --format csv --noquotes)
$k update users/$id --config /tmp/kc.cfg -r EEGFaktura -s email=frieda.huber@eeg-sonnenhang.example -s firstName=Frieda -s lastName=Huber
$k get users/$id --config /tmp/kc.cfg -r EEGFaktura --fields username,email,firstName,lastName
rm -f /tmp/kc.cfg'
