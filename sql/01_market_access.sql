-- Module A: Market Access & Formulary Analysis
-- Identify plans where our drug is restricted vs competitor

SELECT 
    p.plan_type,
    COUNT(DISTINCT c.claim_id) as total_claims,
    SUM(CASE WHEN f.prior_auth_required = 1 THEN 1 ELSE 0 END) as pa_claims,
    ROUND(100.0 * SUM(CASE WHEN f.prior_auth_required = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) as pa_rate_pct,
    AVG(c.copay) as avg_copay,
    f.drug_tier
FROM claims c
JOIN formulary f ON c.ndc = f.ndc AND c.plan_id = f.plan_id
JOIN plans p ON c.plan_id = p.plan_id
GROUP BY p.plan_type, f.drug_tier
HAVING f.drug_tier IN (3, 4)  -- High cost-sharing tiers
ORDER BY pa_rate_pct DESC;
