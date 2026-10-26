-- Demo data for the user-guide screenshots, ONLY for the local eegfaktura-dev stack (fixture world, RC100100).
-- Idempotent. Run once after seeding, e.g.:
--   docker exec -i eegfaktura-legacy-dev-eegfaktura-postgresql-1 psql -v ON_ERROR_STOP=1 -U postgres -d eegfaktura < scripts/prepare-local-stack.sql
-- Never run it against production or pilot.

BEGIN;

-- guard: only the fixture world (RC100100 "Fixture Sonnenhang"); anything else stops before a change
DO $$ BEGIN
  IF NOT EXISTS (SELECT 1 FROM base.eeg WHERE tenant = 'RC100100' AND name = 'Fixture Sonnenhang') THEN
    RAISE EXCEPTION 'not the local fixture stack (RC100100 "Fixture Sonnenhang" missing) — nothing changed';
  END IF;
END $$;

-- the fixture's tariffs have baseFee 2.25, which the backend cannot read (tracking backend 261026-mm1): round all
-- fractional values of RC100100 down
UPDATE base.tariff SET "baseFee" = 2 WHERE tenant = 'RC100100' AND "baseFee" <> trunc("baseFee");

-- a consumer tariff (the fixture has only an archived one)
INSERT INTO base.tariff (id, tenant, type, name, "billingPeriod", "useVat", "vatSupplementaryText", "vatInPercent",
                         "participantFee", "baseFee", "freeKWh", "createdDate", "lastModifiedDate", version,
                         "centPerKWh", discount, status, "inactiveSince", "useMeteringPointFee")
SELECT '00000000-0000-4000-a100-00000000000d', 'RC100100', 'VZP', 'Bezug Standard', 'monthly', true, '', 20,
       0, 0, 0, '2026-01-01', '2026-01-01', 1, 12.5, 0, 'ACTIVE', NULL, false
WHERE NOT EXISTS (SELECT 1 FROM base.tariff WHERE id = '00000000-0000-4000-a100-00000000000d');

-- every active metering point gets a tariff of its direction (overwrites the fixture's assignments on purpose:
-- one consumer had the member tariff), every active member without one the member fee
UPDATE base.meteringpoint SET tariff_id = '00000000-0000-4000-a100-00000000000d'
 WHERE tenant = 'RC100100' AND direction = 'CONSUMPTION' AND status = 'ACTIVE';
UPDATE base.meteringpoint SET tariff_id = '00000000-0000-4000-a100-00000000000b'
 WHERE tenant = 'RC100100' AND direction = 'GENERATION' AND status = 'ACTIVE';
UPDATE base.participant SET "tariffId" = '00000000-0000-4000-a100-00000000000a'
 WHERE tenant = 'RC100100' AND status = 'ACTIVE' AND "tariffId" IS NULL;

-- billing settings of RC100100
INSERT INTO billingj.billing_config (id, tenant_id, before_items_text_invoice, after_items_text_invoice,
       terms_text_invoice, before_items_text_credit_note, after_items_text_credit_note, terms_text_credit_note,
       footer_text, document_number_sequence_length, invoice_number_prefix, invoice_number_start,
       credit_note_number_prefix, credit_note_number_start, date_created, last_updated,
       is_create_credit_notes_for_all_producers)
SELECT gen_random_uuid(), 'RC100100', 'Wir verrechnen dir für den Zeitraum:', 'Danke, dass du Teil unserer Gemeinschaft bist.',
       'Der Betrag wird von deinem Konto abgebucht.', 'Wir schreiben dir für den Zeitraum gut:',
       'Danke für deinen Sonnenstrom.', 'Der Betrag wird auf dein Konto überwiesen.',
       'Fixture Sonnenhang · Hangweg 1 · 8010 Graz', 4, 'RE', 1, 'GS', 1, now(), now(), true
WHERE NOT EXISTS (SELECT 1 FROM billingj.billing_config WHERE tenant_id = 'RC100100');

COMMIT;
