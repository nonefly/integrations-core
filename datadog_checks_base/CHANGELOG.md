# CHANGELOG - datadog_checks

## 1.4.0 / 2018-07-18

* [Fixed] fix packaging of agent requirements. See [#1911](https://github.com/DataDog/integrations-core/pull/1911).
* [Fixed] Properly use skip_proxy for instance configuration. See [#1880](https://github.com/DataDog/integrations-core/pull/1880).
* [Fixed] Sync WMI utils from dd-agent to datadog-checks-base. See [#1897](https://github.com/DataDog/integrations-core/pull/1897).
* [Fixed] Improve check performance by filtering it's input before parsing. See [#1875](https://github.com/DataDog/integrations-core/pull/1875).
* [Changed] Bump prometheus client library to 0.3.0. See [#1866](https://github.com/DataDog/integrations-core/pull/1866).
* [Added] Make HTTP request timeout configurable in prometheus checks. See [#1790](https://github.com/DataDog/integrations-core/pull/1790).

## 1.3.2 / 2018-06-15

* [Changed] Bump requests to 2.19.1. See [#1743](https://github.com/DataDog/integrations-core/pull/1743).

## 1.3.1 / 2018-06-13

* [Fixed] upgrade requests dependency. See [#1734](https://github.com/DataDog/integrations-core/pull/1734).
* [Changed] Set requests stream option to false when scraping Prometheus endpoints. See [#1596](https://github.com/DataDog/integrations-core/pull/1596).

## 1.3.0 / 2018-06-07

* [Fixed] change default value of AgentCheck.check_id for Agent 6. See [#1652](https://github.com/DataDog/integrations-core/pull/1652).
* [Added] Support for gathering metrics from prometheus endpoint for the kubelet itself.. See [#1581](https://github.com/DataDog/integrations-core/pull/1581).
* [Added] include wmi for compat. See [#1565](https://github.com/DataDog/integrations-core/pull/1565).
* [Added] added missing tailfile util. See [#1566](https://github.com/DataDog/integrations-core/pull/1566).
* [Fixed] [base] when running A6, mirror logging behavior. See [#1561](https://github.com/DataDog/integrations-core/pull/1561).

## 1.2.2 / 2018-05-11

* [FEATURE] The generic Prometheus check will now send counter as monotonic counter.
* [BUG] Prometheus requests can use an insecure option
* [BUG] Correctly handle missing counters/strings in PDH checks when possible
* [BUG] Fix Prometheus Scrapper logger
* [SANITY] Clean-up export for `PDHBaseCheck` + export `WinPDHCounter`. [#1183][]
* [IMPROVEMENT] Discard metrics with invalid values

## 1.2.1 / 2018-03-23

* [BUG] Correctly handle internationalized versions of Windows in the PDH library.
* [FEATURE] Keep track of Service Checks in the Aggregator stub.

## 1.1.0 / 2018-03-23

* [FEATURE] Add a generic prometheus check base class & rework prometheus check using a mixin

## 1.0.0 / 2017-03-22

* [FEATURE] adds `datadog_checks`

<!--- The following link definition list is generated by PimpMyChangelog --->
[#1183]: https://github.com/DataDog/integrations-core/issues/1183
