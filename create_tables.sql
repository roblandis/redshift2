CREATE TABLE NetPatientServiceRevenue
(
	PayerType VARCHAR(25) NOT NULL,
	Product VARCHAR(25) NOT NULL,
	Variations VARCHAR(25) NOT NULL,
	CostCenter VARCHAR(25) NOT NULL,
	Entity VARCHAR(25) NOT NULL,
	"Time" BIGINT NOT NULL,
	Datasrc VARCHAR(25) NOT NULL,
	Version VARCHAR(25) NOT NULL,
	Currency VARCHAR(25) NOT NULL,
	Scenario VARCHAR(25) NOT NULL,
	Metrics VARCHAR(25) NOT NULL,
	MetricValue	DOUBLE PRECISION
);


