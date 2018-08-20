# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DotaItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	pass


class DotaMaxItem(scrapy.Item):
	match_id = scrapy.Field()  # 比赛ID
	end_time = scrapy.Field()  # 比赛结束时间
	game_length = scrapy.Field()  # 比赛时长
	match_area = scrapy.Field()  # 匹配的服务器
	first_blood = scrapy.Field()  # 一血时间
	match_level = scrapy.Field()  # 匹配级别
	match_type = scrapy.Field()  # 匹配类型（全阵营，随机？）
	player_camp = scrapy.Field()  # 玩家阵营
	is_win = scrapy.Field()  # 比赛结果（获胜，失败）
	player_id = scrapy.Field()  # 玩家steam_id
	player_name = scrapy.Field()  # 玩家名称
	player_hero = scrapy.Field()  # 玩家所用英雄
	is_mvp = scrapy.Field()  # 是否是MVP
	hero_level = scrapy.Field()  # 玩家英雄等级
	kda = scrapy.Field()  # 玩家KDA
	kda_detail = scrapy.Field()  # 玩家KDA详情
	war_rate = scrapy.Field()  # 参战率
	damage_perc = scrapy.Field()  # 伤害百分比
	dps = scrapy.Field()  # 伤害数值
	last_deny_hit = scrapy.Field()  # 正反补刀数
	exp_pm = scrapy.Field()  # 每分钟经验值
	money_pm = scrapy.Field()  # 每分钟金钱
	damage_build = scrapy.Field()  # 建筑伤害
	milk = scrapy.Field()  # 治疗量

	def get_insert_sql(self):
		insert_sql = "insert into game_match(match_id, end_time, game_length, match_area, first_blood, match_level, \
		match_type, player_camp, is_win, player_id, player_name, player_hero, is_mvp, hero_level, kda, kda_detail, \
		war_rate, damage_perc, dps, last_deny_hit, exp_pm, money_pm, damage_build, milk) \
		VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) \
		ON DUPLICATE KEY UPDATE end_time=VALUES(end_time)"
		params = (
			self["match_id"],
			self["end_time"],
			self["game_length"],
			self["match_area"],
			self["first_blood"],
			self["match_level"],
			self["match_type"],
			self["player_camp"],
			self["is_win"],
			self["player_id"],
			self["player_name"],
			self["player_hero"],
			self["is_mvp"],
			self["hero_level"],
			self["kda"],
			self["kda_detail"],
			self["war_rate"],
			self["damage_perc"],
			self["dps"],
			self["last_deny_hit"],
			self["exp_pm"],
			self["money_pm"],
			self["damage_build"],
			self["milk"],
		)
		return insert_sql, params
