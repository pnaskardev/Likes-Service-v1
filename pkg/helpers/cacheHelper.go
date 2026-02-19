package helpers

import (
	"sync"

	"github.com/redis/go-redis/v9"
)

type Cache struct {
	CacheClient *redis.Client
}

var (
	cache     *Cache
	cacheOnce sync.Once
)

func CacheHelper() (*redis.Client, error) {
	cacheOnce.Do(func() {
		if cache == nil {
			opt, err := redis.ParseURL("redis://<user>:<pass>@localhost:6379/<db>")
			if err != nil {
				panic("REDIS CONNECTION FAILED")
			}

			cache = &Cache{}

			cache.CacheClient = redis.NewClient(opt)
		}
	})

	return cache.CacheClient, nil
}
