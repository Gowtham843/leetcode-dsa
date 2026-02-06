/*
 * 175. Combine Two Tables
 * URL: https://leetcode.com/problems/combine-two-tables/description/
 * Difficulty: Easy
 * Topics: Database
 * Date: 2026-02-06T06:33:45.866Z
 *
 * Table Schemas:
 *
 * +-------------+---------+
 * | Column Name | Type    |
 * +-------------+---------+
 * | personId    | int     |
 * | lastName    | varchar |
 * | firstName   | varchar |
 * +-------------+---------+
 * personId is the primary key (column with unique values) for this table.
 * This table contains information about the ID of some persons and their first and last names.
 *
 * +-------------+---------+
 * | Column Name | Type    |
 * +-------------+---------+
 * | addressId   | int     |
 * | personId    | int     |
 * | city        | varchar |
 * | state       | varchar |
 * +-------------+---------+
 * addressId is the primary key (column with unique values) for this table.
 * Each row of this table contains information about the city and state of one person with ID = PersonId.
 *
 * Input: 
 * Person table:
 * +----------+----------+-----------+
 * | personId | lastName | firstName |
 * +----------+----------+-----------+
 * | 1        | Wang     | Allen     |
 * | 2        | Alice    | Bob       |
 * +----------+----------+-----------+
 * Address table:
 * +-----------+----------+---------------+------------+
 * | addressId | personId | city          | state      |
 * +-----------+----------+---------------+------------+
 * | 1         | 2        | New York City | New York   |
 * | 2         | 3        | Leetcode      | California |
 * +-----------+----------+---------------+------------+
 * Output: 
 * +-----------+----------+---------------+----------+
 * | firstName | lastName | city          | state    |
 * +-----------+----------+---------------+----------+
 * | Allen     | Wang     | Null          | Null     |
 * | Bob       | Alice    | New York City | New York |
 * +-----------+----------+---------------+----------+
 * Explanation: 
 * There is no address in the address table for the personId = 1 so we return null in their city and state.
 * addressId = 1 contains information about the address of personId = 2.
 */

# Write your MySQL query statement below
select p.firstName,p.lastName,a.city,a.state from Person p left join 
address a on p.personId = a.personId
