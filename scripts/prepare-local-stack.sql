-- Demo data for the user-guide screenshots, ONLY for the local eegfaktura-dev stack (fixture world, RC100100).
-- Idempotent. Run it after seeding and before every full screenshot run (it resets the billing history of
-- RC100100, the screenshots bill Jul-Sep 2026 again), e.g.:
--   docker exec -i eegfaktura-legacy-dev-eegfaktura-postgresql-1 psql -v ON_ERROR_STOP=1 -U postgres -d eegfaktura < scripts/prepare-local-stack.sql
-- Never run it against production or pilot. Names, addresses and numbers below are made up.
-- Side effect: RC100100 gets a billing config, so the eegfaktura-dev smoke check „billing config own tenant
-- (none yet → 404)“ answers 200 afterwards.

BEGIN;

-- guard: only the fixture world. RC100100 is checked by its fixture community id and the fixture's fixed member id
-- (00000000-0000-4000-b100-…), which no real community has; both survive the renaming below
DO $$ BEGIN
  IF NOT EXISTS (SELECT 1 FROM base.eeg WHERE tenant = 'RC100100'
                    AND "communityId" = 'AT00800000000RC100100000000000001')
     OR NOT EXISTS (SELECT 1 FROM base.participant WHERE tenant = 'RC100100'
                       AND id = '00000000-0000-4000-b100-000000000001') THEN
    RAISE EXCEPTION 'not the local fixture stack (fixture community RC100100 missing) — nothing changed';
  END IF;
  IF (SELECT count(DISTINCT id) FROM base.tariff WHERE id IN ('00000000-0000-4000-a100-00000000000a',
      '00000000-0000-4000-a100-00000000000b') AND tenant = 'RC100100') <> 2 THEN
    RAISE EXCEPTION 'fixture tariffs of RC100100 missing — nothing changed';
  END IF;
END $$;

-- master data of the community. Grid operator AT008000 = Energienetze Steiermark (eegfaktura-backend config.yaml),
-- matching the metering point prefixes of the fixture
UPDATE base.eeg SET name = 'EEG Sonnenhang', description = 'EEG Sonnenhang', "contactPerson" = 'Frieda Huber',
       email = 'office@eeg-sonnenhang.example', website = 'https://www.eeg-sonnenhang.example',
       phone = '+43 316 123456', "bankName" = 'Musterbank', owner = 'EEG Sonnenhang', bic = 'MUSTATWWXXX',
       "businessNr" = '123456789', "vatNumber" = 'ATU12345678', creditor_id = 'AT12ZZZ00000012345',
       gridoperator_code = 'AT008000', gridoperator_name = 'Energienetze Steiermark GmbH'
 WHERE tenant = 'RC100100';

-- the other fixture communities appear in the community picker and the process images: names without „Fixture“
UPDATE base.eeg SET name = 'GEA Anlagenweg', description = 'GEA Anlagenweg'
 WHERE tenant = 'GC106668' AND "communityId" = 'AT00300000000GC106668000000000001';
UPDATE base.eeg SET name = 'GEA Anlagenweg Stiege 3', description = 'GEA Anlagenweg Stiege 3'
 WHERE tenant = 'GC106668-003' AND "communityId" = 'AT00300000000GC106668000000000003';
UPDATE base.eeg SET name = 'BEG Talweg', description = 'BEG Talweg'
 WHERE tenant = 'RC100200' AND "communityId" = 'AT00800000000RC100200000000000001';
UPDATE base.participant SET firstname = 'Gerda', lastname = 'Lehner' WHERE id = '00000000-0000-4000-b200-000000000001';
UPDATE base.participant SET firstname = 'Stefan', lastname = 'Brunner' WHERE id = '00000000-0000-4000-b300-000000000001';
UPDATE base.participant SET firstname = 'Berta', lastname = 'Koller' WHERE id = '00000000-0000-4000-b400-000000000001';

-- members: the fixture's and those other local test runs added to RC100100 (matched by id or by their metering
-- point; a member that does not exist is skipped)
CREATE TEMP TABLE guide_member (pid uuid, meter text, nr text, firstname text, lastname text, street text,
                                streetnr text, email text, phone text) ON COMMIT DROP;
INSERT INTO guide_member VALUES
  ('00000000-0000-4000-b100-000000000001', NULL, '001', 'Petra', 'Gruber', 'Hangweg', '2', 'petra.gruber@example.org', '+43 664 1234567'),
  ('00000000-0000-4000-b100-000000000002', NULL, '002', 'Bäckerei Hofer GmbH', '', 'Hauptstraße', '12', 'office@baeckerei-hofer.example', '+43 316 765432'),
  ('00000000-0000-4000-b100-000000000003', NULL, '003', 'Anna', 'Steiner', 'Sonnenweg', '7', 'anna.steiner@example.org; familie.steiner@example.org', NULL),
  (NULL, 'AT0080000000000000000000000143001', '004', 'Karl', 'Maier', 'Hangweg', '4', 'karl.maier@example.org', NULL),
  (NULL, 'AT0080000000000000000000000143002', '005', 'Johann', 'Pichler', 'Hangweg', '6', 'johann.pichler@example.org', NULL),
  (NULL, 'AT0080000000000000000000000143003', '006', 'Sabine', 'Wagner', 'Schulgasse', '3', 'sabine.wagner@example.org', NULL),
  ('00000000-0000-4000-bf00-000000000001', NULL, '007', 'Thomas', 'Berger', 'Lindenweg', '1', 'thomas.berger@example.org', NULL),
  ('00000000-0000-4000-bf00-000000000002', NULL, '008', 'Elisabeth', 'Fuchs', 'Lindenweg', '3', 'elisabeth.fuchs@example.org', NULL),
  ('00000000-0000-4000-bf00-000000000003', NULL, '009', 'Martin', 'Leitner', 'Feldgasse', '2', 'martin.leitner@example.org', NULL),
  ('00000000-0000-4000-bf00-000000000004', NULL, '010', 'Claudia', 'Moser', 'Feldgasse', '4', 'claudia.moser@example.org', NULL),
  ('00000000-0000-4000-bf00-000000000005', NULL, '011', 'Stefan', 'Wolf', 'Feldgasse', '6', 'stefan.wolf@example.org', NULL);
UPDATE guide_member g SET pid = m.participant_id FROM base.meteringpoint m
 WHERE g.pid IS NULL AND m.metering_point_id = g.meter AND m.tenant = 'RC100100';
DELETE FROM guide_member g WHERE NOT EXISTS (SELECT 1 FROM base.participant p WHERE p.id = g.pid AND p.tenant = 'RC100100');

UPDATE base.participant p SET "participantNumber" = g.nr, firstname = g.firstname, lastname = g.lastname
  FROM guide_member g WHERE p.id = g.pid;
INSERT INTO base.address (participant_id, type)
SELECT g.pid, k.type FROM guide_member g CROSS JOIN (VALUES ('RESIDENCE'), ('BILLING')) AS k(type)
 WHERE NOT EXISTS (SELECT 1 FROM base.address a WHERE a.participant_id = g.pid AND a.type = k.type);
UPDATE base.address a SET street = g.street, "streetNumber" = g.streetnr, city = 'Graz', zip = '8010'
  FROM guide_member g WHERE a.participant_id = g.pid;
-- a second contact row of a member (fixture: an alternative address) gets a second address
UPDATE base.contactdetail c SET email = CASE WHEN c.email LIKE '%alt%' THEN split_part(g.email, '@', 1) || '@example.com'
                                             ELSE g.email END,
                                phone = CASE WHEN c.email LIKE '%alt%' THEN NULL ELSE g.phone END
  FROM guide_member g WHERE c.participant_id = g.pid;
UPDATE base.bankaccount b SET owner = trim(p.firstname || ' ' || p.lastname), "bankName" = 'Musterbank'
  FROM guide_member g JOIN base.participant p ON p.id = g.pid WHERE b.participant_id = g.pid;
-- the metering points are at the member's address
UPDATE base.meteringpoint m SET street = g.street, "streetNumber" = g.streetnr, city = 'Graz', zip = '8010'
  FROM guide_member g WHERE m.participant_id = g.pid AND m.tenant = 'RC100100';

-- earlier local test runs left placeholder values: an activation date 01.01.1970 and a participation factor of 0 %
-- (the energy data of the demo meters start in 2026, so they are active from 01.01.2026 at the latest)
UPDATE base.meteringpoint SET activesince = least(coalesce("registeredSince", DATE '2026-01-01'), DATE '2026-01-01')
 WHERE tenant = 'RC100100' AND activesince = '1970-01-01';
UPDATE base.metering_partition_factor SET "partFact" = 100 WHERE tenant = 'RC100100' AND "partFact" = 0;

-- the fixture's tariffs have baseFee 2.25, which the backend cannot read (tracking backend 261026-mm1): round all
-- fractional values of RC100100 down
UPDATE base.tariff SET "baseFee" = 2 WHERE tenant = 'RC100100' AND "baseFee" <> trunc("baseFee");

-- tariff names as communities use them
UPDATE base.tariff SET name = 'Mitgliedsbeitrag' WHERE id = '00000000-0000-4000-a100-00000000000a' AND tenant = 'RC100100';
UPDATE base.tariff SET name = 'Einspeisung' WHERE id = '00000000-0000-4000-a100-00000000000b' AND tenant = 'RC100100';
UPDATE base.tariff SET name = 'Bezug 2024' WHERE id = '00000000-0000-4000-a100-00000000000c' AND tenant = 'RC100100';

-- a consumer tariff (the fixture has only an archived one)
INSERT INTO base.tariff (id, tenant, type, name, "billingPeriod", "useVat", "vatSupplementaryText", "vatInPercent",
                         "participantFee", "baseFee", "freeKWh", "createdDate", "lastModifiedDate", version,
                         "centPerKWh", discount, status, "inactiveSince", "useMeteringPointFee")
SELECT '00000000-0000-4000-a100-00000000000d', 'RC100100', 'VZP', 'Bezug Standard', 'monthly', true, '', 20,
       0, 0, 0, '2026-01-01', '2026-01-01', 1, 12.5, 0, 'ACTIVE', NULL, false
WHERE NOT EXISTS (SELECT 1 FROM base.tariff WHERE id = '00000000-0000-4000-a100-00000000000d');

-- every active metering point gets a tariff of its direction (overwrites the fixture's assignments on purpose:
-- one consumer had the member tariff), every active member the member fee
UPDATE base.meteringpoint SET tariff_id = '00000000-0000-4000-a100-00000000000d'
 WHERE tenant = 'RC100100' AND direction = 'CONSUMPTION' AND status = 'ACTIVE';
UPDATE base.meteringpoint SET tariff_id = '00000000-0000-4000-a100-00000000000b'
 WHERE tenant = 'RC100100' AND direction = 'GENERATION' AND status = 'ACTIVE';
UPDATE base.participant SET "tariffId" = '00000000-0000-4000-a100-00000000000a'
 WHERE tenant = 'RC100100' AND status = 'ACTIVE';
-- tariffs other local test runs added to RC100100 are archived (an archived tariff is not listed)
UPDATE base.tariff SET status = 'ARCHIVED'
 WHERE tenant = 'RC100100' AND status <> 'ARCHIVED' AND id NOT IN ('00000000-0000-4000-a100-00000000000a',
       '00000000-0000-4000-a100-00000000000b', '00000000-0000-4000-a100-00000000000c', '00000000-0000-4000-a100-00000000000d');

-- a joining fee with 20 % VAT on the member tariff (web 1.15 / billing 1.6): the member details show its status line
UPDATE base.tariff SET "joiningFee" = 50, "joiningFeeUseVat" = true, "joiningFeeVatInPercent" = 20
 WHERE id = '00000000-0000-4000-a100-00000000000a' AND tenant = 'RC100100' AND type = 'EEG';

-- billing history of RC100100 reset: „Meine Rechnungen“ shows only the documents of the run the screenshots create
CREATE TEMP TABLE guide_files ON COMMIT DROP AS
SELECT file_data_id AS id FROM billingj.billing_document_file WHERE tenant_id = 'RC100100';
DELETE FROM billingj.billing_document_item WHERE billing_document_id IN
       (SELECT id FROM billingj.billing_document WHERE tenant_id = 'RC100100');
DELETE FROM billingj.billing_document_file WHERE tenant_id = 'RC100100';
SELECT lo_unlink(f.data) FROM billingj.file_data f
 WHERE f.id IN (SELECT id FROM guide_files)
   AND EXISTS (SELECT 1 FROM pg_largeobject_metadata l WHERE l.oid = f.data);
DELETE FROM billingj.file_data WHERE id IN (SELECT id FROM guide_files);
DELETE FROM billingj.billing_document WHERE tenant_id = 'RC100100';
DELETE FROM billingj.billing_run WHERE tenant_id = 'RC100100';
DELETE FROM billingj.billing_document_number WHERE tenant_id = 'RC100100';
DELETE FROM billingj.billing_joining_fee_record WHERE tenant_id = 'RC100100';

-- billing settings of RC100100: texts as real EEGs write them (formal, "Text nach Positionen" usually empty);
-- the UPDATE also corrects a stack prepared with the earlier demo texts
INSERT INTO billingj.billing_config (id, tenant_id, footer_text, document_number_sequence_length,
       invoice_number_prefix, invoice_number_start, credit_note_number_prefix, credit_note_number_start,
       date_created, last_updated, is_create_credit_notes_for_all_producers)
SELECT gen_random_uuid(), 'RC100100', '', 4, 'RE', 1, 'GS', 1, now(), now(), true
WHERE NOT EXISTS (SELECT 1 FROM billingj.billing_config WHERE tenant_id = 'RC100100');
UPDATE billingj.billing_config SET
       before_items_text_invoice = 'Wie vereinbart erlauben wir uns folgende Leistungen in Rechnung zu stellen:',
       after_items_text_invoice = NULL,
       terms_text_invoice = 'Der Rechnungsbetrag wird vereinbarungsgemäß von Ihrem Konto abgebucht.',
       before_items_text_credit_note = 'Wie vereinbart erlauben wir uns folgende Leistungen zu vergüten:',
       after_items_text_credit_note = NULL,
       terms_text_credit_note = 'Der Gutschriftsbetrag wird vereinbarungsgemäß auf Ihr Konto überwiesen.',
       before_items_text_info = 'Wie vereinbart erlauben wir uns folgende Leistungen zu vergüten:',
       after_items_text_info = NULL,
       terms_text_info = 'Der Gutschriftsbetrag wird vereinbarungsgemäß auf Ihr Konto überwiesen.',
       footer_text = 'EEG Sonnenhang · Hangweg 1 · 8010 Graz · ZVR 123456789'
 WHERE tenant_id = 'RC100100';

COMMIT;
